from src.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import func

class Task(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    is_completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())