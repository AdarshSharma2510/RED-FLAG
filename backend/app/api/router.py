from fastapi import APIRouter

from app.api.routes import health
from app.api.routes import home

api_router = APIRouter()

api_router.include_router(home.router)
api_router.include_router(health.router)
