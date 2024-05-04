import os
from urllib.parse import urljoin

from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy import UUID
from sqlalchemy.orm import relationship

from server import config
from server.config.database import Base
from server.items_catalog.infrastructure.models.category import Category


class Item(Base):
    __tablename__ = "items_catalog"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    image_url = Column(String)
    description = Column(String, default="")
    category_id = Column(UUID, ForeignKey("items_catalog_category.id"))
    category = relationship(Category, back_populates="items")

    def get_image_dir(self):
        return os.path.join(config.MEDIA_DIR, self.image_url)

    def get_image_url(self) -> str:
        return urljoin(config.MEDIA_URL, self.image_url)
