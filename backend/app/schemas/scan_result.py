from pydantic import BaseModel

from app.schemas.finding import RiskFinding
from app.schemas.ai_response import AIAnalysis


class ScanResult(BaseModel):
    finding: RiskFinding
    analysis: AIAnalysis