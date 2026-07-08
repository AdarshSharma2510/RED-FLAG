from pydantic import BaseModel

from app.schemas.enums import Severity


class AIFinding(BaseModel):
    clause_text: str
    category: str
    severity: Severity
    explanation: str


class AIDetectionResponse(BaseModel):
    findings: list[AIFinding]