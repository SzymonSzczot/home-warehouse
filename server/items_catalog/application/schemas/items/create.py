from pydantic import BaseModel


class ItemCreateSchema(BaseModel):
    name: str

    def to_create(self):
        return {
            "name": self.name
        }
