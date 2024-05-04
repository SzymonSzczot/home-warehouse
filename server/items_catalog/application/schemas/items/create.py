import uuid
from functools import cached_property
from typing import Annotated
from typing import Optional
from typing import Self

from fastapi import File
from fastapi import Form
from fastapi import UploadFile
from pydantic import BaseModel


class ItemCreateSchema(BaseModel):
    name: str
    description: str
    image: Optional[UploadFile] = None

    def to_create(self):
        return {
            "name": self.name,
            "image_url": self.image_filename
        }

    @classmethod
    def as_form(cls, name: str = Form(...), image: Annotated[Optional[UploadFile], File()] = None) ->  Self:
        return cls(name=name, image=image)

    @cached_property
    def image_filename(self):
        return f"{uuid.uuid1()}_{self.image.filename}"
