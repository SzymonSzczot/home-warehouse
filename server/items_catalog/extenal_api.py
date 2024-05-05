from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from starlette import status

from server.items_catalog.application.schemas.categories import CategoryCreateSchema
from server.items_catalog.application.schemas.categories import CategoryListSchema
from server.items_catalog.application.schemas.items import ItemListSchema
from server.items_catalog.application.schemas.items import ItemCreateSchema
from server.items_catalog.infrastructure.repositories.categories import \
    ItemsCatalogCategoryRepository
from server.items_catalog.infrastructure.repositories.items_catalog import ItemsCatalogRepository
import logstash
router = APIRouter()
import logging
host = 'logstash'  # Replace with your Logstash host
port = 50000  # Replace with your Logstash port

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler(host=host, port=port))

# Add a standard output handler
stdout_handler = logging.StreamHandler()
logger.addHandler(stdout_handler)

@router.get("/", response_model=list[ItemListSchema])
async def read_items():
    items = ItemsCatalogRepository().get_items()
    return items


@router.post("/", response_model=ItemListSchema)
async def add_item(item: ItemCreateSchema = Depends(ItemCreateSchema.as_form))-> ItemListSchema:
    logger.info('python-logstash: test logstash info message.')
    item = await ItemsCatalogRepository().add_item(item=item)
    return item


@router.delete("/{item_id}")
async def delete_item(item_id: UUID):
    item = await ItemsCatalogRepository().delete_item(item_id=item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/categories", response_model=list[CategoryListSchema])
async def read_categories():
    return ItemsCatalogCategoryRepository().get_categories()


@router.post("/categories", response_model=CategoryListSchema)
async def add_category(category: CategoryCreateSchema) -> ItemListSchema:
    return ItemsCatalogCategoryRepository().add_category(category=category)
