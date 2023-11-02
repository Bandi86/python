from beanie import Document


class User(Document):
    name: str
    email: str
    password: str
    
    class Config:
        schema_extra = {
            "example": {
                "name": "<NAME>",
                "email": "<EMAIL>",
                "password": "<PASSWORD>"
                }
            }
        
        