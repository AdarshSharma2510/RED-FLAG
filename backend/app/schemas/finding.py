from enum import Enum
from pydantic import BaseModel
from app.schemas.enums import Severity, TriggerSource

class RiskFinding(BaseModel):
    clause_id: int
    sentence_id: int
    matched_text: str
    category: str
    severity: Severity
    explanation: str
    trigger_source: TriggerSource