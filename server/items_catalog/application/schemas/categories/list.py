from uuid import UUID

from pydantic import BaseModel


class CategoryListSchema(BaseModel):
    id: UUID
    name: str
