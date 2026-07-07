from pydantic import BaseModel

from app.schemas.document import ExtractedDocument
from app.schemas.scan_result import ScanResult


class ScanResponse(BaseModel):
    document: ExtractedDocument
    results: list[ScanResult]
    
