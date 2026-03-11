├── aws-monitoring-demo/
│   ├── requirements.txt
│   ├── README.md
│   ├── .env
│   ├── docker/
│   │   └── Dockerfile
│   ├── app/
│   │   ├── config.py
│   │   ├── main.py
│   │   └── websocket_manager.py
│   │   ├── utils/
│   │   │   └── logger.py
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── styles.css
│   │   │   ├── js/
│   │   │   │   └── dashboard.js
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── templates/
│   │   │   └── dashboard.html
│   │   ├── workers/
│   │   │   └── scheduler.py
│   │   ├── services/
│   │   │   ├── metrics.py
│   │   │   ├── event_router.py
│   │   │   ├── anomaly.py
│   │   │   ├── health_checker.py
│   │   │   └── alerting.py
│   │   ├── aws_simulator/
│   │   │   ├── lambda_handler.py
│   │   │   ├── eventbridge.py
│   │   │   ├── cloudwatch.py
│   │   │   └── sns.py
