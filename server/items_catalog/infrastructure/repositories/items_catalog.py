import uuid

from server import config
from server.config.database import DbSession
from server.items_catalog.application.schemas.items import ItemCreateSchema
from server.items_catalog.infrastructure.models.items_catalog import Item
from server.utils.files import save_upload_file


class ItemsCatalogRepository:
    def __init__(self):
        self.db = DbSession()

    def get_items(self, skip: int = 0, limit: int = 100):
        with self.db as db:
            return db.query(Item).offset(skip).limit(limit).all()

    async def add_item(self, item: ItemCreateSchema):
        with self.db as db:
            file_name = await save_upload_file(filename=item.image_filename, upload_file=item.image, dest_folder=config.MEDIA_DIR)
            db_item = Item(id=uuid.uuid4(), **item.to_create())
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            return db_item
