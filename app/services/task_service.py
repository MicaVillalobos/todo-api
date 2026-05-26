from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.task import Task
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, db: Session):
        self.repository = TaskRepository(db)

    def get_all(self) -> list[Task]:
        return self.repository.get_all()

    def get_by_id(self, task_id: int) -> Task:
        task = self.repository.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {task_id} not found",
            )
        return task

    def create(self, task_data: TaskCreate) -> Task:
        return self.repository.create(task_data)

    def update(self, task_id: int, task_data: TaskUpdate) -> Task:
        task = self.get_by_id(task_id)
        return self.repository.update(task, task_data)

    def delete(self, task_id: int) -> None:
        task = self.get_by_id(task_id)
        self.repository.delete(task)
