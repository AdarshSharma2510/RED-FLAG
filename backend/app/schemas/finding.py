from enum import Enum
from pydantic import BaseModel


class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class TriggerSource(str, Enum):
    RULE_ENGINE = "RULE_ENGINE"
    LLM = "LLM"
    BOTH = "BOTH"

class RiskFinding(BaseModel):
    sentence_id: int

    matched_text: str

    category: str

    severity: Severity

    explanation: str

    trigger_source: TriggerSource