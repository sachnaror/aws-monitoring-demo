from app.utils.logger import get_logger

logger = get_logger(__name__)

alerts = []


def send_alert(message):

    alert = {
        "message": message
    }

    alerts.append(alert)

    logger.warning(f"SNS ALERT: {message}")


def get_alerts():

    return alerts
