"""Configuration settings for the Zep Demo application."""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # API Keys
    anam_api_key: str
    zep_api_key: str
    openrouter_api_key: str

    # Anam AI Configuration (for avatar/voice only - we use custom LLM)
    anam_api_base_url: str = "https://api.anam.ai"
    anam_avatar_id: str
    anam_voice_id: str

    # Zep Config
    zep_docs_user_id: str

    # Deployment URLs
    frontend_url: str = "http://localhost:8501"
    backend_url: str = "http://localhost:8000"

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"


# Global settings instance
settings = Settings()
