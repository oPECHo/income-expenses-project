from fastapi import FastAPI
from .core import models
from .core.database import engine
from .routers import transaction, users

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(users.router)
app.include_router(transaction.router)
