from enum import Enum
from pydantic import BaseModel
from app.schemas.enums import Severity

class Rule(BaseModel):
    name : str
    category : str
    severity : Severity
    
    explanation : str
    
    patterns : list[str]
