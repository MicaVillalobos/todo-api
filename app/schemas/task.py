from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import Priority, TaskStatus


#Base con campos comunes
class TaskBase(BaseModel):
    title: str
    description: str | None = None

#Esquema para crear una tarea
class TaskCreate(TaskBase):
    pass    

#Esquema para actualizar una tarea
class TaskUpdate(TaskBase):
    title: str | None = None
    description: str | None  = None
    status: TaskStatus | None  = None
    priority: Priority | None = None

#Esquema para mostrar una tarea
class TaskResponse(TaskBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: TaskStatus
    priority: Priority
    created_at: datetime
    updated_at: datetime