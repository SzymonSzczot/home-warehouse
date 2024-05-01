from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from config.database import get_db
from items_catalog.infrastructure.models.items_catalog import Item
from items_catalog.infrastructure.repositories.items_catalog import ItemsCatalogRepository

router = APIRouter()

@router.get("/", response_model=list[Item])
async def read_items(db: Session = Depends(get_db)):
    items = ItemsCatalogRepository(db=db).get_items()
    return items


@router.post("/", response_model=Item)
async def add_item():
    pass
