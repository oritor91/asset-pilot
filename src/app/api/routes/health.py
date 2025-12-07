"""Health endpoints for service monitoring."""

from fastapi import APIRouter, status

router = APIRouter(prefix="/health", tags=["Health"])


@router.get(
    "/live",
    status_code=status.HTTP_200_OK,
)
async def get_liveness() -> dict[str, str]:
    """Return a simple liveness payload for monitoring.

    Returns:
        dict[str, str]: Payload describing the current liveness state.
    """
    return {"status": "Healthy"}
