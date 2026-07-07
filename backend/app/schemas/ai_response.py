from pydantic import BaseModel, Field

class AIAnalysis(BaseModel):
    risk_summary: str = Field(description="Short summary of the legal risk")
    legal_consequence: str = Field(description= "Potential legal consequence")
    recommendation: str = Field(description= "Recommendation for the user")
    confidence: float = Field(description="Confidence score between 0 and 1")
    
    