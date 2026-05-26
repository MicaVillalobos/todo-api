from sqlalchemy import Column, DateTime, Enum, Integer, String, Text, func

from app.core.database import Base
from app.models.enums import Priority, TaskStatus


# Modelo de la tabla tasks
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(
        Enum(TaskStatus),
        default=TaskStatus.PENDING,
        nullable=False,
        server_default=TaskStatus.PENDING,
    )
    priority = Column(
        Enum(Priority),
        default=Priority.MEDIUM,
        nullable=False,
        server_default=Priority.MEDIUM,
    )
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )
