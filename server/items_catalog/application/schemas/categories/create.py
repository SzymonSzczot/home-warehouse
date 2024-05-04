from pydantic import BaseModel


class CategoryCreateSchema(BaseModel):
    name: str

    def to_create(self):
        return {
            "name": self.name
        }
