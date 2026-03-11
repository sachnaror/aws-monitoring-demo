from app.utils.logger import get_logger

logger = get_logger(__name__)


def detect_anomaly(latency: float):

    if latency > 3:
        logger.warning(f"Anomaly detected: latency {latency}")

        return True

    return False
