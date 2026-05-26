from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Task]:
        return self.db.query(Task).all()

    def get_by_id(self, task_id: int):
        return self.db.query(Task).filter(Task.id == task_id).first()

    def create(self, task_data: TaskCreate) -> Task:
        task = Task(**task_data.model_dump())
        # para convertir el Pydantic a un dict y luego a un modelo SQLAlchemy y los ** para pasar los campos como argumentos
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update(self, task: Task, task_data: TaskUpdate) -> Task:
        update_data = task_data.model_dump(exclude_unset=True)
        # para obtener solo los campos que se han actualizado, el exclude unset es para no incluir los campos que no vienen del front
        for field, value in update_data.items():
            setattr(task, field, value)
        # recorre los campos actualizados y los asigna a la tarea usando setattr, que es una función de Python para asignar atributos dinámicamente
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task: Task) -> None:
        self.db.delete(task)
        self.db.commit()
