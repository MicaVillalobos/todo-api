from fastapi import FastAPI

from app.routers.task_router import router as task_router

# main.py es el punto de entrada de la aplicación,
# donde se crea la instancia de FastAPI y se incluyen los routers para las rutas de la API.
# Es donde se arranca la api y se registran los routers.

app = FastAPI(
    title="Todo API", description="A simple API for managing tasks", version="1.0.0"
)
# title para el nombre de la API,
# description para una breve descripción y
#  version para la versión de la API en /docs de Swagger.

app.include_router(task_router)


def main():
    print("Hello from todo-api!")


if __name__ == "__main__":
    main()
