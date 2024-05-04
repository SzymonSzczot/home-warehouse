from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy import UUID
from sqlalchemy.orm import relationship

from server.config.database import Base
from server.items_catalog.infrastructure.models.category import Category


class Item(Base):
    __tablename__ = "items_catalog"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    image_url = Column(String)
    description = Column(String)
    category_id = Column(UUID, ForeignKey("items_catalog_category.id"))
    category = relationship(Category, back_populates="items")
