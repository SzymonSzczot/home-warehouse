from sqlalchemy import Column, Integer, String

from server.main import Base


class Item(Base):
    __tablename__ = "items_catalog"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
