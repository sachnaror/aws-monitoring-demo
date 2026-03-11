let latencyChart;


// Initialize chart
function initChart() {

    const ctx = document.getElementById("latencyChart");

    latencyChart = new Chart(ctx, {

        type: "line",

        data: {
            labels: [],
            datasets: [{
                label: "Latency (seconds)",
                data: [],
                borderColor: "#007bff",
                backgroundColor: "rgba(0,123,255,0.15)",
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


// Update chart
function updateChart(metrics) {

    if (!latencyChart) return;

    const labels = [];
    const latency = [];

    metrics.slice(-20).forEach(m => {

        const time = new Date(m.timestamp * 1000);

        labels.push(
            time.getHours() + ":" +
            time.getMinutes() + ":" +
            time.getSeconds()
        );

        latency.push(m.latency);

    });

    latencyChart.data.labels = labels;
    latencyChart.data.datasets[0].data = latency;

    latencyChart.update();

}


// Update services table
function updateServices(metrics) {

    const tableBody = document.querySelector("#servicesTable tbody");

    if (!tableBody) return;

    tableBody.innerHTML = "";

    metrics.forEach(service => {

        const row = document.createElement("tr");

        const statusColor = service.status === "OK" ? "green" : "red";

        row.innerHTML = `
            <td>${service.service}</td>
            <td style="color:${statusColor};font-weight:bold">${service.status}</td>
            <td>${service.latency}s</td>
        `;

        tableBody.appendChild(row);

    });

}


// Update alerts
function updateAlerts(alerts) {

    const list = document.getElementById("alertsList");

    if (!list) return;

    list.innerHTML = "";

    alerts.slice().reverse().forEach(alert => {

        const item = document.createElement("li");

        let color = "list-group-item-warning";

        if (alert.severity === "critical")
            color = "list-group-item-danger";

        item.className = "list-group-item " + color;

        item.innerText = alert.message;

        list.appendChild(item);

    });

}


// Update overview cards
function updateOverview(metrics, alerts) {

    const serviceCount = document.getElementById("serviceCount");
    const alertCount = document.getElementById("alertCount");
    const avgLatency = document.getElementById("avgLatency");

    if (serviceCount)
        serviceCount.innerText = metrics.length;

    if (alertCount)
        alertCount.innerText = alerts.length;

    let totalLatency = 0;

    metrics.forEach(m => totalLatency += m.latency);

    let avg = metrics.length ? (totalLatency / metrics.length).toFixed(2) : 0;

    if (avgLatency)
        avgLatency.innerText = avg + " s";

}


// Fetch metrics
async function fetchMetrics() {

    const response = await fetch("/metrics");

    const data = await response.json();

    return data.metrics || [];

}


// Fetch alerts
async function fetchAlerts() {

    const response = await fetch("/alerts");

    const data = await response.json();

    return data.alerts || [];

}


// Refresh dashboard
async function refreshDashboard() {

    try {

        const metrics = await fetchMetrics();
        const alerts = await fetchAlerts();

        updateServices(metrics);
        updateAlerts(alerts);
        updateOverview(metrics, alerts);
        updateChart(metrics);

    }
    catch (err) {

        console.error("Dashboard refresh error:", err);

    }

}


// Optional WebSocket support
function connectWebSocket() {

    try {

        const socket = new WebSocket("ws://localhost:8000/ws");

        socket.onmessage = function (event) {

            const data = JSON.parse(event.data);

            if (data.metrics) {

                updateChart(data.metrics);

            }

        };

    } catch (e) {

        console.log("WebSocket not available, using polling.");

    }

}


// Start dashboard
function startDashboard() {

    initChart();

    connectWebSocket();

    refreshDashboard();

    setInterval(refreshDashboard, 4000);

}


document.addEventListener("DOMContentLoaded", startDashboard);
