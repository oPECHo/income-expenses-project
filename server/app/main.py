from fastapi import FastAPI
from .core import models
from .core.database import engine
from .routers import transaction

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(transaction.router)
