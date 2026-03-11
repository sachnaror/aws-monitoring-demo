import threading
import time

from app.services.health_checker import check_services
from app.utils.logger import get_logger

logger = get_logger(__name__)

_scheduler_lock = threading.Lock()
_scheduler_started = False


def monitoring_loop():
    logger.info("Monitoring scheduler running (3s interval)")

    while True:
        try:
            check_services()
        except Exception as e:
            logger.error(f"Monitoring error: {e}")

            time.sleep(3)


def start_scheduler():
    global _scheduler_started

    with _scheduler_lock:
        if _scheduler_started:
            logger.info("Scheduler already running, skipping startup")
            return

        _scheduler_started = True

        thread = threading.Thread(target=monitoring_loop, daemon=True)
        thread.start()

        logger.info(f"Scheduler thread started (id={thread.ident})")
