from src.database.db import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, relationship


class Habit(Base):
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), ondelete="CASCADE")

    user: Mapped["User"] = relationship(
        "User",
        back_populates="habits",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
