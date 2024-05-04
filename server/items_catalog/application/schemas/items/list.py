from uuid import UUID

from pydantic import BaseModel


class ItemListSchema(BaseModel):
    id: UUID
    name: str
