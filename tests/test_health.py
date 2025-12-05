"""Health endpoint tests."""

import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.anyio
async def test_liveness_endpoint_returns_ok() -> None:
    """Ensure the /health/live endpoint returns a 200 response with expected payload."""
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

