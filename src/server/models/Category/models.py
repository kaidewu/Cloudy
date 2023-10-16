from pydantic import BaseModel

class CreateCategory(BaseModel):
    categoryName: str