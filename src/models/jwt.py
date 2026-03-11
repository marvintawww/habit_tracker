from src.database.db import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime
from datetime import datetime, timezone


class JWTBlacklist(Base):
    __tablename__ = "jwt_blacklist"

    id: Mapped[int] = mapped_column(primary_key=True)
    jti: Mapped[str] = mapped_column(unique=True)
    blacklisted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"TOKEN(id={self.id}, jti={self.jti})"
