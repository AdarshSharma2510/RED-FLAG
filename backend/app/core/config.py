# This is done to get the env file things into a function so that you can call them as per need using the Settings instance created here

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    app_version: str

    model_name: str

    database_url: str

    gemini_api_key: str

    huggingface_access_token : str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()