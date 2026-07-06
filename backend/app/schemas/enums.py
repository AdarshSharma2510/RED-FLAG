from enum import Enum

class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class TriggerSource(str, Enum):
    RULE_ENGINE = "RULE_ENGINE"
    LLM = "LLM"
    BOTH = "BOTH"