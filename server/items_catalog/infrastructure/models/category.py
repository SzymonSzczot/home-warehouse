from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import UUID
from sqlalchemy.orm import relationship

from server.config.database import Base


class Category(Base):
    __tablename__ = "items_catalog_category"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    items = relationship("Item", back_populates="category")
