from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {
        "Message" : "Welcome to RED FLAG API",
        "version" : "1.0.0", 
    }
