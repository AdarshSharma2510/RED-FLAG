from pydantic import BaseModel

from app.schemas.ai_response import AIAnalysis


class AIAnalysisBatch(BaseModel):
    analyses: list[AIAnalysis]