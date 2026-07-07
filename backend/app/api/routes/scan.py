from pathlib import Path
import shutil
import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.scan_response import ScanResponse
from app.services.scan.scan_service import ScanService

router = APIRouter(prefix="/scan", tags=["Scan"])


@router.post(
    "/",
    response_model=ScanResponse,
    summary="Scan a legal contract",
    description="Uploads a contract, analyzes it using rule-based detection and Gemini AI, and returns detected risks.",
)
async def scan_contract(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file uploaded.",
        )

    allowed_extensions = {".pdf", ".docx", ".txt"}

    suffix = Path(file.filename).suffix.lower()

    if suffix not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX, and TXT files are supported.",
        )

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_path = Path(temp_file.name)

    try:
        scan_service = ScanService()
        response = scan_service.scan(temp_path)
        response.document.filename = file.filename
        return response

    finally:
        if temp_path.exists():
            temp_path.unlink()

        await file.close()