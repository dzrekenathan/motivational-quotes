from fastapi import FastAPI
from .routers import quotes
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(quotes.router)