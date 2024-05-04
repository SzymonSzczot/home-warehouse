from fastapi import APIRouter

from server.items_catalog.application.schemas.categories import CategoryCreateSchema
from server.items_catalog.application.schemas.categories import CategoryListSchema
from server.items_catalog.application.schemas.items import ItemListSchema
from server.items_catalog.application.schemas.items import ItemCreateSchema
from server.items_catalog.infrastructure.repositories.categories import \
    ItemsCatalogCategoryRepository
from server.items_catalog.infrastructure.repositories.items_catalog import ItemsCatalogRepository

router = APIRouter()

@router.get("/", response_model=list[ItemListSchema])
async def read_items():
    items = ItemsCatalogRepository().get_items()
    return items


@router.post("/", response_model=ItemListSchema)
async def add_item(item: ItemCreateSchema) -> ItemListSchema:
    item = ItemsCatalogRepository().add_item(item=item)
    return item

@router.get("/categories", response_model=list[CategoryListSchema])
async def read_categories():
    return ItemsCatalogCategoryRepository().get_categories()


@router.post("/categories", response_model=CategoryListSchema)
async def add_category(category: CategoryCreateSchema) -> ItemListSchema:
    return ItemsCatalogCategoryRepository().add_category(category=category)
