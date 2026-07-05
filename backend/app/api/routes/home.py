from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {
        "Message" : "RED FLAG API" 
    }
