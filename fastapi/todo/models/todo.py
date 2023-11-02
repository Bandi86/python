from beanie import Document
from pydantic import BaseModel

class Todo(Document):
    user: str
    title: str
    description: str
    completed: bool = False
    
    class Config:
        schema_extra = {
            "example": {
                "user": "John Doe",
                "title": "Buy Milk",
                "description": "Buy Milk",
                "completed": False
            }
        }
        
class TodoUpdate(BaseModel):
    user: str
    title: str
    description: str
    completed: bool = False
    
    class Config:
        schema_extra = {
            "example": {
                "user": "John Doe",
                "title": "Buy Milk",
                "description": "Buy Milk",
                "completed": False
            }
        }