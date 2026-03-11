import requests
import time
from app.utils.logger import get_logger
from app.aws_simulator.cloudwatch import publish_metric

logger = get_logger(__name__)

SERVICES = [
    {"name": "auth-service", "url": "https://httpbin.org/status/200"},
    {"name": "payment-service", "url": "https://httpbin.org/delay/1"},
    {"name": "email-service", "url": "https://httpbin.org/status/200"},
]


def check_services():

    results = []

    for service in SERVICES:
        start = time.time()

        try:
            r = requests.get(service["url"], timeout=3)
            latency = round(time.time() - start, 2)

            status = "OK" if r.status_code == 200 else "FAIL"

        except Exception:
            latency = 0
            status = "FAIL"

        logger.info(f"{service['name']} | {status} | {latency}s")

        publish_metric(service["name"], latency, status)

        results.append({
            "service": service["name"],
            "status": status,
            "latency": latency
        })

    return results
