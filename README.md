# ☁️ AWS Monitoring Demo (FastAPI)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Async-green)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-orange)
![Monitoring](https://img.shields.io/badge/Observability-Demo-purple)

------------------------------------------------------------------------

## 🚀 Overview

**AWS Monitoring Demo** is a lightweight observability playground built
with **FastAPI**.\

It simulates a cloud monitoring system similar to **AWS CloudWatch,
EventBridge, SNS, and Lambda**.

The project demonstrates how real monitoring systems work:
```
• Service health checks\
• Metrics collection\
• Alert generation\
• Event routing\
• Real‑time dashboards\
• WebSocket live updates
```
Think of it as a **mini CloudWatch + Datadog demo built in Python**.

------------------------------------------------------------------------

## 🎬 Demo Video

<div align="center">
<a href="https://youtu.be/WZ16FErIzr8">
<img src="" alt="Watch the demo" width="600" height="600" />
</a>
</div>



------------------------------------------------------------------------



------------------------------------------------------------------------

## 🧠 What This Project Demonstrates

This project simulates a full monitoring architecture.
```
    Services → Metrics → CloudWatch → EventBridge → Alerts → Dashboard
```
It helps understand how observability systems work internally.

------------------------------------------------------------------------

## 🏗 Architecture
```
    ┌──────────────┐
    │ Microservices│
    └──────┬───────┘
           │ health checks
           ▼
    ┌──────────────┐
    │ Metrics      │
    │ Collector    │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ CloudWatch   │
    │ Simulator    │
    └──────┬───────┘
           │ events
           ▼
    ┌──────────────┐
    │ EventBridge  │
    │ Router       │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ SNS Alerts   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ Dashboard    │
    │ (WebSocket)  │
    └──────────────┘
```
------------------------------------------------------------------------

## ⚙️ Features

### 🔎 Service Monitoring

Simulated microservices are monitored periodically.

Metrics collected:
```
• latency\
• cpu usage\
• memory usage\
• service status
```
------------------------------------------------------------------------

### 📊 Metrics Dashboard

Real‑time dashboard shows:
```
• average latency\
• service health\
• active alerts\
• historical metrics
```
Charts update automatically using **WebSockets**.

------------------------------------------------------------------------

### 🚨 Alert System

Alerts trigger automatically when thresholds are crossed.

Examples:
```
• High latency\
• CPU spike\
• Memory spike\
• Service downtime
```
------------------------------------------------------------------------

### 🔁 Event‑Driven Pipeline

The monitoring flow simulates AWS services:
```
  AWS Service   In This Demo
  ------------- ---------------------
  CloudWatch    Metrics storage
  EventBridge   Event routing
  SNS           Alert notifications
  Lambda        Automated actions
```
------------------------------------------------------------------------

## 📂 Project Structure
```
    aws-monitoring-demo/
    │
    ├── requirements.txt
    ├── README.md
    ├── .env
    │
    ├── docker/
    │   └── Dockerfile
    │
    ├── app/
    │   ├── main.py
    │   ├── config.py
    │   ├── websocket_manager.py
    │
    │   ├── utils/
    │   │   └── logger.py
    │
    │   ├── api/
    │   │   └── routes.py
    │
    │   ├── workers/
    │   │   └── scheduler.py
    │
    │   ├── services/
    │   │   ├── health_checker.py
    │   │   ├── alerting.py
    │   │   ├── metrics.py
    │   │   ├── event_router.py
    │   │   └── anomaly.py
    │
    │   ├── aws_simulator/
    │   │   ├── cloudwatch.py
    │   │   ├── eventbridge.py
    │   │   ├── sns.py
    │   │   └── lambda_handler.py
    │
    │   ├── templates/
    │   │   └── dashboard.html
    │
    │   └── static/
    │       ├── css/
    │       │   └── styles.css
    │       └── js/
    │           └── dashboard.js
```

------------------------------------------------------------------------

## 🛠 Installation

Clone the repo
```
    git clone https://github.com/your-repo/aws-monitoring-demo.git
    cd aws-monitoring-demo
```
Install dependencies
```
    pip install -r requirements.txt
```
Run the application
```
    uvicorn app.main:app
```
Open in browser
```
    http://127.0.0.1:8000
```
------------------------------------------------------------------------

## 🐳 Docker Support

Build image
```
    docker build -t aws-monitoring-demo .
```
Run container
```
    docker run -p 8000:8000 aws-monitoring-demo
```
------------------------------------------------------------------------

## 💡 Example Alerts
```
    payment-service latency exceeded threshold
    order-service CPU spike detected
    auth-service memory usage high
    email-service service DOWN
```
------------------------------------------------------------------------

## 📈 Future Improvements

Ideas to extend this demo:
```
• integrate real AWS CloudWatch\
• add Grafana dashboards\
• integrate Prometheus metrics\
• add Kubernetes health probes\
• add AI anomaly detection
```
------------------------------------------------------------------------

## 📩 Contact

| Name              | Details                             |
|-------------------|-------------------------------------|
| **👨‍💻 Developer**  | Sachin Arora                      |
| **📧 Email**      | [sachnaror@gmail.com](mailto:sacinaror@gmail.com) |
| **📍 Location**   | Noida, India                       |
| **📂 GitHub**     | [github.com/sachnaror](https://github.com/sachnaror) |
| **🌐 Youtube**    | [about.me/sachin-arora](https://www.youtube.com/@sachnaror4841/videos) |
| **🌐 Blog**       | [about.me/sachin-arora](https://medium.com/@schnaror) |
| **🌐 Website**    | [about.me/sachin-arora](https://about.me/sachin-arora) |
| **🌐 Twitter**    | [about.me/sachin-arora](https://twitter.com/sachinhep) |
| **📱 Phone**      | [+91 9560330483](tel:+919560330483) |


------------------------------------------------------------------------

## ⭐ If you like this project

Give it a ⭐ on GitHub.

It helps others discover it.

------------------------------------------------------------------------
