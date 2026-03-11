from app.utils.logger import get_logger

logger = get_logger(__name__)


def lambda_handler(event_type: str, service: str):

    logger.info(f"Lambda triggered | event={event_type} | service={service}")

    if event_type == "SERVICE_FAILURE":
        logger.warning(f"Lambda remediation: restarting {service}")

    if event_type == "HIGH_LATENCY":
        logger.warning(f"Lambda remediation: scaling {service}")
