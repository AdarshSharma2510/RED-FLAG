from pathlib import Path
import shutil
import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.scan.scan_service import ScanService

router = APIRouter(prefix="/scan", tags=["Scan"])

@router.post("/")
async def scan_contract(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file uploaded.",
        )

    suffix = Path(file.filename).suffix

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_path = Path(temp_file.name)

    try:
        scan_service = ScanService()
        response = scan_service.scan(temp_path)
        return response

    finally:
        if temp_path.exists():
            temp_path.unlink()
            
            