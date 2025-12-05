"""Application entrypoint for the Asset Pilo FastAPI AWS SAM template."""

from functools import lru_cache

from fastapi import FastAPI
from mangum import Mangum

from app.api.routes import api_router
from app.core.settings import Settings, get_settings


@lru_cache
def create_application() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns:
        FastAPI: FastAPI application configured with routers and metadata.
    """
    settings = get_settings()
    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=settings.app_description,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
    )
    application.include_router(api_router)
    return application


app = create_application()
lambda_handler = Mangum(app)

__all__ = ["app", "create_application", "lambda_handler"]

