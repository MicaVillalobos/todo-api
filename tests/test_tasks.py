from fastapi import status


def test_create_task(client):
    """POST /tasks/ - Crear una nueva tarea"""
    response = client.post("/tasks/", 
                           json={"title": "Test Task", "description": "This is a test task"})
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert data["status"] == "pending"
    assert data["priority"] == "medium"
    assert "id" in data
    assert "created_at" in data

def test_get_all_tasts_empty(client):
    """GET /tasks/ - devuelve lista vacía si no hay tareas"""
    response = client.get("/tasks/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

def test_get_all_tasks(client):
    """GET /tasks/ - devuelve todas las tareas"""
    # Crear varias tareas
    client.post("/tasks/", json={"title": "Task 1"})
    client.post("/tasks/", json={"title": "Task 2"})

    response = client.get("/tasks/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2

def test_get_task_by_id(client):
    """GET /tasks/{task_id} - devuelve tarea por ID"""
    # Crear una tarea
    created = client.post("/tasks/", json={"title": "Task 1", "description": "First task"}).json()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == created["id"]
    assert data["title"] == "Task 1"
    assert data["description"] == "First task"

def test_update_task(client):
    """PUT /tasks/{task_id} - actualiza una tarea existente"""
    # Crear una tarea
    created = client.post("/tasks/", json={"title": "Task 1", "description": "First task"}).json()

    # Actualizar la tarea
    response = client.put(f"/tasks/{created['id']}", 
                          json={"title": "Updated Task", "description": "Updated description", "status": "in_progress", "priority": "high"})

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == created["id"]
    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated description"
    assert data["status"] == "in_progress"
    assert data["priority"] == "high"

def test_delete_task(client):
    """DELETE /tasks/{task_id} - elimina una tarea"""
    # Crear una tarea
    created = client.post("/tasks/", json={"title": "Task to Delete", "description": "This task will be deleted"}).json()

    # Eliminar la tarea
    response = client.delete(f"/tasks/{created['id']}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verificar que la tarea ya no existe
    get_response = client.get(f"/tasks/{created['id']}")
    assert get_response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_task_not_found(client):
    """DELETE /tasks/{task_id} - intenta eliminar una tarea que no existe"""
    response = client.delete("/tasks/9999")
    assert response.status_code == status.HTTP_404_NOT_FOUND