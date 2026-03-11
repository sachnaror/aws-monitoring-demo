from apscheduler.schedulers.background import BackgroundScheduler
from app.services.health_checker import check_services
from app.utils.logger import get_logger

logger = get_logger(__name__)

scheduler = BackgroundScheduler()


def start_scheduler():

    logger.info("Starting monitoring scheduler")

    scheduler.add_job(
        check_services,
        "interval",
        seconds=10
    )

    scheduler.start()
