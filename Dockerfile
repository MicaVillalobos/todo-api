# Imagen base de Python
FROM python:3.12-slim

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos de dependencias primero
# (Docker cachea capas — si no cambiaron las deps, no las reinstala)
COPY pyproject.toml uv.lock ./

# Instalar dependencias de producción
RUN uv sync --frozen --no-dev

# Copiar el resto del código
COPY . .

# Puerto que expone la app
EXPOSE 8000

# Comando para arrancar la app
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
