from typing import Optional
from urllib.parse import urljoin
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field
from pydantic import computed_field

from server import config


class ItemListSchema(BaseModel):
    id: UUID
    name: str
    image_url: Optional[str] = Field(exclude=True)

    @computed_field
    @property
    def picture_url(self) -> str:
        if not self.image_url:
              return ""
        print(config.MEDIA_URL)
        print(self.image_url)
        return urljoin(config.MEDIA_URL, self.image_url)
