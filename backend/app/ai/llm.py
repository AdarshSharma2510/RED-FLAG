from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from app.core.config import settings

class LLM:
    def __init__(self):
        # self.model = ChatGoogleGenerativeAI(
        #     model=settings.model_name,
        #     google_api_key=settings.gemini_api_key,
        #     temperature=0.2,
        # )
        endpoint = HuggingFaceEndpoint(
            repo_id = 'deepseek-ai/DeepSeek-V4-Flash',
            task = 'text-generation',
            huggingfacehub_api_token= settings.huggingface_access_token
        )
        
        self.model = ChatHuggingFace(
            llm = endpoint,
            temperature = 0.2
        )
        
    def invoke(self, prompt):
        return self.model.invoke(prompt)
