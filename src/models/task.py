from src.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import func, ForeignKey

class Task(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    is_completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner = relationship("src.models.user.User", back_populates='tasks')