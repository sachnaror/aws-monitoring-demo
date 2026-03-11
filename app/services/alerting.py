from app.aws_simulator.sns import send_alert
from app.utils.logger import get_logger

logger = get_logger(__name__)


def trigger_alert(message: str):

    logger.warning(f"Alert triggered: {message}")

    send_alert(message)
