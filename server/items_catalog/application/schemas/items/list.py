from pydantic import BaseModel


class ItemListSchema(BaseModel):
    id: int
    name: str


class ItemCreateSchema(BaseModel):
    name: str
