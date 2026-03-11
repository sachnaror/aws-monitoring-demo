from app.utils.logger import get_logger
from app.aws_simulator.eventbridge import send_event

logger = get_logger(__name__)

LATENCY_THRESHOLD = 2


def publish_metric(service, latency, status):

    logger.info(f"CloudWatch metric received: {service} latency={latency}")

    if status == "FAIL":
        send_event("SERVICE_FAILURE", service)

    if latency > LATENCY_THRESHOLD:
        send_event("HIGH_LATENCY", service)
