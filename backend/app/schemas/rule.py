from enum import Enum
from pydantic import BaseModel

class Severity(str, Enum):
    LOW = "LOW",
    MEDIUM = "MEDIUM",
    HIGH = "HIGH"

class Rule(BaseModel):
    name : str
    category : str
    severity : Severity
    
    explanation : str
    
    patterns : list[str]
    
