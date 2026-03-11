from fastapi import APIRouter
from app.aws_simulator.sns import get_alerts
from app.services.metrics import get_metrics

router = APIRouter()


@router.get("/alerts")
def alerts():
    return {"alerts": get_alerts()}


@router.get("/metrics")
def metrics():
    return {"metrics": get_metrics()}
