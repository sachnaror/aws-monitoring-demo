# AWS Monitoring Demo (FastAPI)

A demo monitoring and alerting platform built using Python and FastAPI.

The project simulates AWS monitoring architecture including:

- CloudWatch metrics
- EventBridge event routing
- SNS notifications
- Lambda automation
- Health checks
- Monitoring dashboards

The goal is to demonstrate observability, alerting, and automation workflows.

---

## Architecture

Service Health Check
↓
CloudWatch Metrics
↓
EventBridge Rules
↓
Lambda Automation
↓
SNS Alerts
↓
Monitoring Dashboard

---

## Features

- FastAPI backend
- Monitoring dashboard (Bootstrap UI)
- Background monitoring jobs
- Alert simulation
- Event-driven architecture
- AWS-like monitoring pipeline

---

## Run locally

Install dependencies

```bash
pip install -r requirements.txt
