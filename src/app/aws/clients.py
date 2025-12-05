"""AWS client helpers."""

from functools import lru_cache
from typing import Final

from boto3 import Session
from botocore.client import BaseClient

from app.core.settings import get_settings

DEFAULT_SERVICE_REGION: Final[str] = "us-east-1"


@lru_cache
def get_boto3_session() -> Session:
    """Return a cached boto3 session using configured credentials.

    Returns:
        Session: boto3 session initialised with application settings.
    """
    settings = get_settings()
    return Session(region_name=settings.aws_region or DEFAULT_SERVICE_REGION)


def get_lambda_client(session: Session | None = None) -> BaseClient:
    """Return a Lambda client using the provided or cached session.

    Args:
        session (Session | None): Optional boto3 session to reuse.

    Returns:
        BaseClient: Configured Lambda client instance.
    """
    current_session = session or get_boto3_session()
    return current_session.client("lambda")


__all__ = ["DEFAULT_SERVICE_REGION", "get_boto3_session", "get_lambda_client"]

