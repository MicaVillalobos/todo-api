# Todo API 🚀

> REST API para gestión de tareas construida con FastAPI, PostgreSQL y Clean Architecture.

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/MicaVillalobos/todo-api/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/MicaVillalobos/todo-api/tree/main)
[![Coverage Status](https://coveralls.io/repos/github/MicaVillalobos/todo-api/badge.svg?branch=main)](https://coveralls.io/github/MicaVillalobos/todo-api?branch=main)
[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED)](https://www.docker.com/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

## 📋 Índice

- [Descripción](#-descripción)
- [Features](#-features)
- [Entidades](#️-entidades)
- [Stack tecnológico](#️-stack-tecnológico)
- [Prerequisitos](#-prerequisitos)
- [Cómo correr la app](#-cómo-correr-la-app)
- [Cómo correr los tests](#-cómo-correr-los-tests)
- [Cómo instalar los hooks](#️-cómo-instalar-los-hooks)
- [Estándares aplicados](#-estándares-aplicados)
- [Rutas de la API](#️-rutas-de-la-api)
- [Variables de entorno](#-variables-de-entorno)
- [Deployment](#️-deployment)
- [Areas to improve](#-areas-to-improve)
- [Author](#️-author)

---

## 📖 Descripción

API REST para gestión de tareas que permite crear, leer, actualizar y eliminar tareas con diferentes estados y prioridades. Construida siguiendo Clean Architecture y buenas prácticas de desarrollo.

---

## ✨ Features

- CRUD completo de tareas
- Estados de tarea: `PENDING`, `IN_PROGRESS`, `DONE`
- Prioridades: `LOW`, `MEDIUM`, `HIGH`
- Validación automática de datos con Pydantic
- Documentación automática en `/docs`
- Migraciones de base de datos con Alembic
- Tests de integración con 100% de coverage
- Dockerizado con PostgreSQL

---

## 🗃️ Entidades

### Task

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Integer | Clave primaria autoincremental |
| `title` | String(100) | Título de la tarea (requerido) |
| `description` | Text | Descripción detallada (opcional) |
| `status` | Enum | Estado: `PENDING`, `IN_PROGRESS`, `DONE` |
| `priority` | Enum | Prioridad: `LOW`, `MEDIUM`, `HIGH` |
| `created_at` | DateTime | Fecha de creación (automático) |
| `updated_at` | DateTime | Fecha de última modificación (automático) |

---

## 🛠️ Stack tecnológico

| Tecnología | Versión | Uso |
|---|---|---|
| **Python** | 3.12 | Lenguaje principal |
| **FastAPI** | 0.115 | Framework web |
| **PostgreSQL** | 16 | Base de datos producción |
| **SQLite** | - | Base de datos para tests |
| **SQLAlchemy** | 2.0 | ORM |
| **Alembic** | 1.13 | Migraciones de BD |
| **Pydantic** | 2.0 | Validación de datos |
| **Pytest** | 7.0 | Testing |
| **Ruff** | 0.4 | Linting y formatting |
| **Docker** | - | Containerización |
| **UV** | - | Gestor de dependencias |

---

## 📋 Prerequisitos

- [Docker](https://www.docker.com/) y Docker Compose

Para desarrollo local también necesitás:
- [Python 3.12+](https://www.python.org/)
- [UV](https://docs.astral.sh/uv/)

---

## 🚀 Cómo correr la app

### Con Docker (recomendado)

**1. Clonar el repositorio**
```bash
git clone https://github.com/MicaVillalobos/todo-api.git
cd todo-api
```

**2. Configurar variables de entorno**

Mac/Linux:
```bash
cp .env.example .env
```

Windows:
```bash
copy .env.example .env
```

**3. Levantar la aplicación**

Mac/Linux:
```bash
./up_dev.sh
```

Windows:
```bash
docker-compose up --build
```
> 💡 Al levantar con Docker, las migraciones y el seed se ejecutan automáticamente.

La API estará disponible en:
- **API:** http://localhost:8000
- **Documentación interactiva:** http://localhost:8000/docs

### Sin Docker (desarrollo local)

**1. Instalar dependencias**
```bash
uv sync
```

**2. Configurar variables de entorno**

Mac/Linux:
```bash
cp .env.example .env
```

Windows:
```bash
copy .env.example .env
```

**3. Correr migraciones**
```bash
uv run alembic upgrade head
```

**4. Cargar datos de prueba (opcional)**
```bash
uv run python seed.py
```

**5. Levantar la app**
```bash
uv run fastapi dev main.py
```

---

## 🧪 Cómo correr los tests

**Instalar dependencias de desarrollo**
```bash
uv sync
```

**Correr tests**
```bash
uv run pytest tests/ -v
```

**Correr tests con coverage**
```bash
uv run pytest tests/ -v --cov=app --cov-report=term-missing
```

---

## 🪝 Cómo instalar los hooks

Los hooks verifican automáticamente el código antes de cada commit.

**Instalar dependencias de desarrollo**
```bash
uv sync
```

**Instalar los hooks**
```bash
uv run pre-commit install
```

**Verificar manualmente**
```bash
uv run pre-commit run --all-files
```

---

## 📐 Estándares aplicados

- **Clean Architecture** — Separación en capas: Router → Service → Repository
- **SOLID** — Single Responsibility en cada capa
- **DRY** — Sin repetición de código, herencia en schemas
- **Ruff** — Linting y formatting automático
- **Pre-commit hooks** — Verificación antes de cada commit
- **Conventional Commits** — Mensajes de commit estandarizados (`feat:`, `fix:`, `chore:`)
- **Variables de entorno** — Sin credenciales en el código
- Se utilizó SQLAlchemy como ORM en modo sincrónico y Alembic para el versionado de migraciones de base de datos.

---

## 🛣️ Rutas de la API

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/tasks` | Obtener todas las tareas |
| `GET` | `/tasks/{id}` | Obtener tarea por ID |
| `POST` | `/tasks` | Crear nueva tarea |
| `PUT` | `/tasks/{id}` | Actualizar tarea |
| `DELETE` | `/tasks/{id}` | Eliminar tarea |

Documentación completa disponible en http://localhost:8000/docs

---

## 🔐 Variables de entorno

| Variable | Descripción | Ejemplo |
|---|---|---|
| `DATABASE_URL` | URL de conexión a la DB | `postgresql://user:pass@localhost/db` |
| `SECRET_KEY` | Clave secreta de la app | `supersecret123` |
| `ENV` | Entorno de ejecución | `development` |
| `PORT` | Puerto de la app | `8000` |

---

## 🚢 Deployment

La API está deployada en Render:
- **API:** https://todo-api-a9vs.onrender.com
- **Docs:** https://todo-api-a9vs.onrender.com/docs

---

## 🔮 Areas to improve

- [ ] Autenticación JWT
- [ ] Paginación en listado de tareas
- [ ] Filtros por status y priority
- [ ] Relación con usuarios
- [ ] Rate limiting
- [ ] Cache con Redis

---

## 👩‍💻 Author

**Micaela**
- GitHub: [@MicaVillalobos](https://github.com/MicaVillalobos)
