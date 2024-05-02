from typing import List

from server.config.database import DbSession
from server.items_catalog.application.schemas.items.list import ItemCreateSchema
from server.items_catalog.infrastructure.models.items_catalog import Item


class ItemsCatalogRepository:
    def __init__(self):
        self.db = DbSession()

    def get_items(self, skip: int = 0, limit: int = 100):
        with self.db as db:
            return db.query(Item).offset(skip).limit(limit).all()

    def add_items(self, items: List[ItemCreateSchema]):
        with self.db as db:
            for item in items:
                db.add(item)
                db.commit()
                db.refresh(item)
            return items
