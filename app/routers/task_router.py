from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])
# prefijo para todas las rutas de tareas y etiqueta para la documentación de Swagger


def get_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)


@router.get("/", response_model=list[TaskResponse])
def get_all_tasks(service: TaskService = Depends(get_service)):
    return service.get_all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, service: TaskService = Depends(get_service)):
    return service.get_by_id(task_id)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, service: TaskService = Depends(get_service)):
    return service.create(task_data)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int, task_data: TaskUpdate, service: TaskService = Depends(get_service)
):
    return service.update(task_id, task_data)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, service: TaskService = Depends(get_service)):
    service.delete(task_id)
    return None
