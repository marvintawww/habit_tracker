from fastapi import FastAPI
from src.routes.v1.__init__ import router as main_router

app = FastAPI(
    title="Habit Tracker",
    description="Habit Tracker Description",
    version="0.0.1",
)

app.include_router(main_router)
