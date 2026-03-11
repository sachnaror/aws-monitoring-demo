let chart;

function initChart() {

    const ctx = document.getElementById("latencyChart");

    chart = new Chart(ctx, {

        type: "line",

        data: {
            labels: [],
            datasets: [{
                label: "Latency (seconds)",
                data: [],
                borderColor: "blue",
                backgroundColor: "rgba(0,123,255,0.1)",
                tension: 0.3,
                fill: true
            }]
        },

        options: {
            responsive: true,
            animation: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }

    });

}


function updateChart(latency) {

    const time = new Date().toLocaleTimeString();

    chart.data.labels.push(time);
    chart.data.datasets[0].data.push(latency);

    if (chart.data.labels.length > 20) {

        chart.data.labels.shift();
        chart.data.datasets[0].data.shift();

    }

    chart.update();
}


function loadMetrics(metrics) {

    const table = document.querySelector("#servicesTable tbody");

    table.innerHTML = "";

    metrics.forEach(item => {

        const row = document.createElement("tr");

        const color = item.status === "OK" ? "green" : "red";

        row.innerHTML = `
            <td>${item.service}</td>
            <td style="color:${color};font-weight:bold">${item.status}</td>
            <td>${item.latency}s</td>
        `;

        table.appendChild(row);

        updateChart(item.latency);

    });

}


function loadAlerts(alerts) {

    const list = document.getElementById("alertsList");

    list.innerHTML = "";

    alerts.slice().reverse().forEach(alert => {

        const item = document.createElement("li");

        item.className = "list-group-item alert-item";

        item.innerText = alert.message;

        list.appendChild(item);

    });

}


function updateOverview(metrics, alerts) {

    document.getElementById("serviceCount").innerText = metrics.length;

    document.getElementById("alertCount").innerText = alerts.length;

    let total = 0;

    metrics.forEach(m => total += m.latency);

    let avg = metrics.length ? (total / metrics.length).toFixed(2) : 0;

    document.getElementById("avgLatency").innerText = avg + " s";

}


function connectWebSocket() {

    const socket = new WebSocket("ws://localhost:8000/ws");

    socket.onmessage = function (event) {

        const data = JSON.parse(event.data);

        if (data.latency) {

            updateChart(data.latency);

        }

    };

    socket.onerror = function () {
        console.log("WebSocket connection error");
    }

}


async function refreshDashboard() {

    try {

        const metricsResponse = await fetch("/metrics");
        const metricsData = await metricsResponse.json();

        const alertsResponse = await fetch("/alerts");
        const alertsData = await alertsResponse.json();

        loadMetrics(metricsData.metrics);
        loadAlerts(alertsData.alerts);

        updateOverview(metricsData.metrics, alertsData.alerts);

    }
    catch (error) {

        console.error("Dashboard refresh failed:", error);

    }

}


function startDashboard() {

    initChart();

    connectWebSocket();

    refreshDashboard();

    setInterval(refreshDashboard, 4000);

}


document.addEventListener("DOMContentLoaded", startDashboard);
