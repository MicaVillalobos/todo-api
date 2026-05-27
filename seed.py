from datetime import UTC, datetime

from app.core.database import Base, SessionLocal, engine
from app.models.enums import Priority, TaskStatus
from app.models.task import Task

Base.metadata.create_all(bind=engine)

now = datetime.now(UTC)

tasks = [
    Task(
        title="Diseñar base de datos",
        description="Definir modelos y relaciones",
        status=TaskStatus.DONE,
        priority=Priority.HIGH,
        created_at=now,
        updated_at=now,
    ),
    Task(
        title="Implementar API REST",
        description="Crear endpoints con FastAPI",
        status=TaskStatus.IN_PROGRESS,
        priority=Priority.HIGH,
        created_at=now,
        updated_at=now,
    ),
    Task(
        title="Escribir tests",
        description="Tests de integración con pytest",
        status=TaskStatus.PENDING,
        priority=Priority.MEDIUM,
        created_at=now,
        updated_at=now,
    ),
    Task(
        title="Dockerizar la app",
        description="Crear Dockerfile y docker-compose",
        status=TaskStatus.PENDING,
        priority=Priority.LOW,
        created_at=now,
        updated_at=now,
    ),
]


def seed():
    print("🌱 Iniciando seed...")
    db = SessionLocal()
    try:
        existing = db.query(Task).first()
        if existing:
            print("⚠️  La base de datos ya tiene datos, saltando seed...")
            return

        for task in tasks:
            db.add(task)

        db.commit()
        print(f"✅ {len(tasks)} tareas creadas exitosamente!")

    except Exception as e:
        db.rollback()
        print(f"❌ Error al crear el seed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
