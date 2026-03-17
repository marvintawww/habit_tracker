from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.routes.v1.__init__ import router as main_router
from src.database.db import db
from src.models.user import User
from src.models.jwt import JWTBlacklist

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.create_tables()
    yield
    await db.engine.dispose()


app = FastAPI(
    title="Habit Tracker",
    description="Habit Tracker Description",
    version="0.0.1",
)

app.include_router(main_router)
