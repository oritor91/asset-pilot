from fastapi import APIRouter
from app.models.property import Property
from app.aws.property_table import PropertyTable

router = APIRouter(prefix="/property", tags=["Property"])

@router.post("/create")
async def create_property(property: Property) -> None:
    PropertyTable.insert_new_property(property)
    return {"message": "Property created successfully"}