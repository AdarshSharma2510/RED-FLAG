from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Red Flag API",
    description="AI-powered legal contract analyzer",
    version="1.0.0",
)

app.include_router(api_router)