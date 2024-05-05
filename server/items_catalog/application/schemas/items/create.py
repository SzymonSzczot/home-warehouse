import uuid
from functools import cached_property
from typing import Self
from typing import Union

from fastapi import Form
from fastapi import UploadFile
from pydantic import BaseModel


class ItemCreateSchema(BaseModel):
    name: str
    description: str = ""
    image: Union[None, UploadFile] = None

    def to_create(self):
        return {
            "name": self.name,
            "description": self.description,
            "image_url": self.image_filename
        }

    @classmethod
    def as_form(cls, image: Union[str, None, UploadFile] = None, name: str = Form(...), description: str = Form(default="")) ->  Self:
        if image == "null":
            image = None
        return cls(image=image, name=name, description=description)

    @cached_property
    def image_filename(self):
        if not self.image:
            return ""
        return f"{uuid.uuid1()}_{self.image.filename}"
