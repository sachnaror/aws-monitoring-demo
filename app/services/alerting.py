from collections import deque
from threading import Lock


# store last 100 alerts
alerts_store = deque(maxlen=100)

alerts_lock = Lock()


def create_alert(service: str, message: str, severity: str = "warning"):
    """
    Simulates SNS alert generation
    """

    alert = {
        "service": service,
        "message": message,
        "severity": severity
    }

    with alerts_lock:
        alerts_store.append(alert)


def get_alerts():
    """
    Return all alerts
    """

    with alerts_lock:
        return list(alerts_store)


def clear_alerts():
    """
    Utility for testing
    """

    with alerts_lock:
        alerts_store.clear()
