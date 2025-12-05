"""Application configuration settings."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
        validate_assignment=True,
    )

    environment: str = Field(
        default="local",
        description="Deployment environment name such as local, dev, prod.",
    )
    app_name: str = Field(default="Asset Pilo FastAPI Service", description="API title.")
    app_version: str = Field(default="0.1.0", description="Semantic version used for docs.")
    app_description: str = Field(
        default="FastAPI template deployed with AWS SAM and API Gateway.",
        description="Human readable API description rendered in docs.",
    )
    docs_url: str | None = Field(
        default="/docs",
        description="Path where the Swagger UI is served. Set to None to disable.",
    )
    redoc_url: str | None = Field(
        default="/redoc",
        description="Path where the ReDoc UI is served. Set to None to disable.",
    )
    aws_region: str = Field(default="us-east-1", description="AWS region for service clients.")


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings instance.

    Returns:
        Settings: Fully configured settings object.
    """
    return Settings()


__all__ = ["Settings", "get_settings"]

