from contextlib import asynccontextmanager

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


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting monitoring system...")
    start_scheduler()
    yield
    logger.info("Stopping monitoring system...")


# IMPORTANT: app must be global
app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(router)


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "app_name": settings.APP_NAME
        }
    )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except Exception:
        manager.disconnect(websocket)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": settings.APP_NAME
    }
