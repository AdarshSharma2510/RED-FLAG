from app.ai.llm import LLM
from app.ai.prompt_builder import PromptBuilder

from app.schemas.ai_detection import AIDetectionResponse
from app.schemas.document import ExtractedDocument


class GeminiDetector:
    def __init__(self):
        self.llm = LLM(AIDetectionResponse)

    def detect(self, document: ExtractedDocument) -> AIDetectionResponse:
        prompt = PromptBuilder.build_detection(document)
        return self.llm.invoke(prompt)