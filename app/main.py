from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.workers.scheduler import start_scheduler
from app.config import settings
from app.utils.logger import get_logger
from app.websocket_manager import manager
from app.api.routes import router

logger = get_logger(__name__)

app = FastAPI(title=settings.APP_NAME)

# Start monitoring scheduler
@app.on_event("startup")
def start_monitoring():
    logger.info("Starting monitoring system...")
    start_scheduler()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Include API routes
app.include_router(router)


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):

    logger.info("Dashboard opened")

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "app_name": settings.APP_NAME
        }
    )


# WebSocket endpoint for real-time updates
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()

    except:
        manager.disconnect(websocket)


@app.get("/health")
def health():

    logger.info("Health check OK")

    return {
        "status": "ok",
        "service": settings.APP_NAME
    }
