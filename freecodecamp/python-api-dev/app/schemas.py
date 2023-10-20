from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  # optional field with true

class PostCreate(PostBase):
    pass

    