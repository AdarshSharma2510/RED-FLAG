from app.ai.llm import LLM
from app.ai.prompt_builder import PromptBuilder
from app.schemas.ai_response import AIAnalysis
from app.schemas.finding import RiskFinding


class AnalysisService:
    def __init__(self):
        self.llm = LLM()

    def analyze(self, finding: RiskFinding) -> AIAnalysis:
        prompt = PromptBuilder.build(finding)

        response = self.llm.invoke(prompt)

        return response
    