import random
import time
import itertools

from app.utils.logger import get_logger
from app.aws_simulator.cloudwatch import publish_metric
from app.services.alerting import create_alert

logger = get_logger(__name__)

SERVICES = [
    "auth-service",
    "payment-service",
    "email-service",
    "order-service",
    "notification-service"
]

service_cycle = itertools.cycle(SERVICES)


def generate_latency():
    return round(random.uniform(0.1, 2.5), 2)


def generate_cpu():
    return random.randint(10, 95)


def generate_memory():
    return random.randint(20, 90)


def check_services():

    service = next(service_cycle)

    latency = generate_latency()
    cpu = generate_cpu()
    memory = generate_memory()

    status = "OK"

    if random.random() < 0.05:
        status = "DOWN"

        metric = {
            "service": service,
            "latency": latency,
            "cpu": cpu,
            "memory": memory,
            "status": status,
            "timestamp": time.time()
        }

        publish_metric(metric)

        logger.info(f"{service} latency={latency}s cpu={cpu}% mem={memory}%")

        if latency > 1.5:
            create_alert(service, f"{service} latency high ({latency}s)", "warning")

            if cpu > 85:
                create_alert(service, f"{service} CPU spike ({cpu}%)", "critical")

                if memory > 80:
                    create_alert(service, f"{service} memory usage high ({memory}%)", "warning")

                    if status == "DOWN":
                        create_alert(service, f"{service} service is DOWN", "critical")
