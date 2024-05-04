import sys
from os.path import dirname

from starlette.staticfiles import StaticFiles

sys.path.append(dirname(__file__))

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from config.database import engine
from config.database import Base
from items_catalog.extenal_api import router as items_catalog_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck", response_model=dict)
def healthcheck(skip: int = 0, limit: int = 100):
    return {"status": "ok"}

app.mount("/media", StaticFiles(directory="media"), name="media")


app.include_router(items_catalog_router, prefix="/api/items-catalog")
