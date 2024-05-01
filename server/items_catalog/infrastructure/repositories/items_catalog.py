from server.items_catalog.infrastructure.models.items_catalog import Item


class ItemsCatalogRepository:
    def __init__(self, *, db):
        self.db = db
    def get_items(self, skip: int = 0, limit: int = 100):
        return self.db.query(Item).offset(skip).limit(limit).all()
