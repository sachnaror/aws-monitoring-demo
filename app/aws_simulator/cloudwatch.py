from collections import deque
from threading import Lock


# store last 500 metrics
metrics_store = deque(maxlen=500)

metrics_lock = Lock()


def publish_metric(metric: dict):
    """
    Simulates CloudWatch metric publishing
    """

    with metrics_lock:
        metrics_store.append(metric)


def get_metrics():
    """
    Returns all stored metrics
    """

    with metrics_lock:
        return list(metrics_store)


def get_latest_metrics():
    """
    Returns latest metric per service
    """

    latest = {}

    with metrics_lock:
        for metric in metrics_store:
            latest[metric["service"]] = metric

            return list(latest.values())
