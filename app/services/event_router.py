from app.utils.logger import get_logger
from app.aws_simulator.lambda_handler import lambda_handler
from app.services.alerting import trigger_alert

logger = get_logger(__name__)


def route_event(event_type: str, service: str):

    logger.info(f"Routing event {event_type} for {service}")

    lambda_handler(event_type, service)

    if event_type == "SERVICE_FAILURE":
        trigger_alert(f"{service} failed")

    if event_type == "HIGH_LATENCY":
        trigger_alert(f"{service} latency exceeded threshold")
