import uuid

from server.config.database import DbSession
from server.items_catalog.application.schemas.categories import CategoryCreateSchema
from server.items_catalog.infrastructure.models.category import Category


class ItemsCatalogCategoryRepository:
    def __init__(self):
        self.db = DbSession()

    def get_categories(self, skip: int = 0, limit: int = 100):
        with self.db as db:
            return db.query(Category).offset(skip).limit(limit).all()

    def add_category(self, category: CategoryCreateSchema):
        with self.db as db:
            db_category = Category(id=uuid.uuid4(), **category.to_create())
            db.add(db_category)
            db.commit()
            db.refresh(db_category)
            return db_category
