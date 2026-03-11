from fastapi import APIRouter
from app.aws_simulator.cloudwatch import get_metrics
from app.services.alerting import get_alerts

router = APIRouter()


@router.get("/metrics")
def metrics():
    return {"metrics": get_metrics()}


@router.get("/alerts")
def alerts():
    return {"alerts": get_alerts()}
