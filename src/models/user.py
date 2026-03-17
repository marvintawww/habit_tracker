from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.habit import Habit

from src.database.db import Base


from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    firstname: Mapped[str]
    lastname: Mapped[str]
    hashed_password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    is_active: Mapped[bool] = mapped_column(default=True)
    habits: Mapped[list["Habit"]] = relationship(
        "Habit",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self):
        return f"User(id={self.id}, login={self.login})"
