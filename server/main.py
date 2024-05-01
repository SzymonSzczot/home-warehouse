import sys
from os.path import dirname
sys.path.append(dirname(__file__))


from fastapi import FastAPI
from config.database import engine
from config.database import Base
from items_catalog.extenal_api import router as items_catalog_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/healthcheck", response_model=dict)
def healthcheck(skip: int = 0, limit: int = 100):
    return {"status": "ok"}


app.include_router(items_catalog_router, prefix="/api/items-catalog")
