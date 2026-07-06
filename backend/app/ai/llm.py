from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from app.core.config import settings

llm = HuggingFaceEndpoint(
    repo_id='Deepseek-ai/DeepSeek-V4-Flash',
    task = 'text-generation'
)

class LLM:
    def __init__(self):
        # self.model = ChatGoogleGenerativeAI(
        #     model=settings.model_name,
        #     google_api_key=settings.gemini_api_key,
        #     temperature=0.2,
        # )
        
        self.model = ChatHuggingFace(
            llm = llm,
            temperature = 0.2,
            huggingface_access_token = settings.huggingface_access_token
        )
        
    def invoke(self, prompt):
        return self.model.invoke(prompt)
