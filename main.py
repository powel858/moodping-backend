import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from moodping.config.settings import get_settings
from moodping.config.mysql_config import engine, Base

from moodping.kakao_authentication.controller.kakao_authentication_controller import (
    router as kakao_auth_router,
    kakao_redirect_router,
)
from moodping.authentication.controller.authentication_controller import router as auth_router
from moodping.account.controller.account_controller import account_router
from moodping.mood_record.controller.mood_record_controller import mood_record_router
from moodping.mood_analysis.controller.mood_analysis_controller import mood_analysis_router
from moodping.weekly_report.controller.weekly_report_controller import weekly_report_router
from moodping.event_log.controller.event_log_controller import event_log_router

import moodping.account.domain.entity.account         # noqa: F401
import moodping.mood_record.domain.entity.mood_record  # noqa: F401
import moodping.mood_analysis.domain.entity.mood_analysis  # noqa: F401
import moodping.weekly_report.domain.entity.weekly_report  # noqa: F401
import moodping.event_log.domain.entity.event_log      # noqa: F401

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

STATIC_DIR = Path(__file__).resolve().parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    logger.info("MoodPing FastAPI 시작. LLM_PROVIDER=%s", settings.llm_provider)
    Base.metadata.create_all(bind=engine)
    yield
    logger.info("MoodPing FastAPI 종료.")


app = FastAPI(
    title="MoodPing API",
    description="감정 기록 및 AI 분석 웹앱 백엔드 (Domain-Driven)",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(kakao_auth_router)
app.include_router(kakao_redirect_router)
app.include_router(auth_router)
app.include_router(mood_record_router)
app.include_router(mood_analysis_router)
app.include_router(weekly_report_router)
app.include_router(event_log_router)
app.include_router(account_router)

if STATIC_DIR.exists():
    app.mount("/css", StaticFiles(directory=STATIC_DIR / "css"), name="css")
    app.mount("/js", StaticFiles(directory=STATIC_DIR / "js"), name="js")
    if (STATIC_DIR / "images").exists():
        app.mount("/images", StaticFiles(directory=STATIC_DIR / "images"), name="images")


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/record", include_in_schema=False)
def record():
    return FileResponse(STATIC_DIR / "record.html")


@app.get("/record.html", include_in_schema=False)
def record_legacy():
    return FileResponse(STATIC_DIR / "record.html")


@app.get("/report", include_in_schema=False)
def report():
    return FileResponse(STATIC_DIR / "report.html")
