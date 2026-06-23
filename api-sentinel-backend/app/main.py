from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.scans import router as scans_router

app =FastAPI(
    title="API Sentinel"
)

app.include_router(
    health_router,
    prefix="/api/v1"
)

app.include_router(
    scans_router,
    prefix="/ap1/v1",
    tags=["Scans"],
)