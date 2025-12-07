from pydantic import BaseModel

class Property(BaseModel):
    property_id: str
    holding_entity_id: str
    property_name: str
    property_address: str
    property_city: str
    property_state: str
    property_zip: str