import os
from pynamodb.models import Model
from pynamodb import attributes
from app.models.property import Property

class PropertyTable(Model):
    class Meta:
        table_name = os.getenv("PROPERTY_TABLE_NAME")
        region = "us-east-1"

    property_id = attributes.UnicodeAttribute(hash_key=True)
    holding_entity_id = attributes.UnicodeAttribute(range_key=True)
    property_name = attributes.UnicodeAttribute()
    property_address = attributes.UnicodeAttribute()
    property_city = attributes.UnicodeAttribute()
    property_state = attributes.UnicodeAttribute()
    property_zip = attributes.UnicodeAttribute()
    
    @classmethod
    def insert_new_property(cls, property: Property) -> None:
        cls(
            property_id=property.property_id,
            holding_entity_id=property.holding_entity_id,
            property_name=property.property_name,
            property_address=property.property_address,
            property_city=property.property_city,
            property_state=property.property_state,
            property_zip=property.property_zip
        ).save()