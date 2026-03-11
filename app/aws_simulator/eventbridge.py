from app.utils.logger import get_logger
from app.aws_simulator.sns import send_alert

logger = get_logger(__name__)


def send_event(event_type, service):

    logger.info(f"EventBridge event: {event_type} from {service}")

    if event_type == "SERVICE_FAILURE":
        send_alert(f"{service} service failure detected")

    if event_type == "HIGH_LATENCY":
        send_alert(f"{service} latency threshold exceeded")
