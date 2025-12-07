"""Application entrypoint for the Asset Pilo FastAPI AWS SAM template."""

from fastapi import FastAPI
from mangum import Mangum

from app.api.routes.property import router as property_router
from app.api.routes.health import router as health_router

app = FastAPI(
    title="Asset Pilo FastAPI",
    version="0.1.0",
    description="FastAPI application packaged as a Lambda function.",
    root_path="/Prod"
)

app.include_router(health_router)
app.include_router(property_router)


@app.get("/debug")
async def debug() -> dict[str, str]:
    return {"status": "Debug"}


lambda_handler = Mangum(app)


