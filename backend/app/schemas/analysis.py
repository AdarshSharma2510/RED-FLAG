from pydantic import BaseModel

from app.schemas.document import ExtractedDocument
from app.schemas.finding import RiskFinding, Severity

class AnalysisResult(BaseModel):
    document: ExtractedDocument
    overall_severity: Severity
    summary: str
    findings: list[RiskFinding]
    
