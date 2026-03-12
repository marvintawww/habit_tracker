import os

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/habits"
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7
