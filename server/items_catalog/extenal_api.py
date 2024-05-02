from fastapi import APIRouter

from server.items_catalog.application.schemas.items import ItemListSchema
from server.items_catalog.application.schemas.items.list import ItemCreateSchema
from server.items_catalog.infrastructure.repositories.items_catalog import ItemsCatalogRepository

router = APIRouter()

@router.get("/", response_model=list[ItemListSchema])
async def read_items():
    items = ItemsCatalogRepository().get_items()
    return items


@router.post("/", response_model=ItemListSchema)
async def add_item(item: ItemCreateSchema) -> ItemListSchema:
    items = ItemsCatalogRepository().add_items([item])
    return items[0]
