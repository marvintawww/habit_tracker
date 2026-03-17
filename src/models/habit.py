from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.user import User

from src.database.db import Base


from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Habit(Base):
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship("User", back_populates="habits")
