from app.ai.llm import LLM
from app.ai.prompt_builder import PromptBuilder

from app.schemas.analysis_batch import AIAnalysisBatch
from app.schemas.finding import RiskFinding


class AnalysisService:
    def __init__(self):
        self.llm = LLM(AIAnalysisBatch)

    def analyze(self, findings: list[RiskFinding]):
        prompt = PromptBuilder.build_batch(findings)

        response = self.llm.invoke(prompt)

        return response.analyses