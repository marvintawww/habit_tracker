import os

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/habits"
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
