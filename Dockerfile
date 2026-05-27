# Imagen base — Python 3.12 versión slim (liviana, sin extras innecesarios)
# slim pesa ~150MB vs la versión completa que pesa ~900MB
FROM python:3.12-slim

# Copiamos el binario de UV desde su imagen oficial
# Es más rápido que instalarlo con pip
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Directorio de trabajo dentro del contenedor
# Todo lo que hagamos de acá en adelante es relativo a /app
WORKDIR /app

# Copiamos PRIMERO solo los archivos de dependencias
# Esto aprovecha el cache de Docker — si no cambiaron las deps,
# no las reinstala en cada build (ahorra tiempo)
COPY pyproject.toml uv.lock ./

# Instalamos solo las dependencias de producción (sin pytest, ruff, etc)
# --frozen → usa exactamente las versiones del uv.lock
# --no-dev → no instala dependencias de desarrollo
RUN uv sync --frozen --no-dev

# Copiamos el resto del código DESPUÉS de instalar deps
# Si cambiás código pero no deps, Docker usa el cache de la capa anterior
COPY . .

# Le decimos a Docker que la app escucha en el puerto 8000
# (es informativo, no abre el puerto solo)
EXPOSE 8000

# Comando que se ejecuta cuando arranca el contenedor
# Primero corre las migraciones, después arranca la app
# --host 0.0.0.0 → acepta conexiones desde cualquier IP (necesario en Docker)
# --port 8000 → puerto donde escucha
CMD ["sh", "-c", "uv run alembic upgrade head && uv run uvicorn main:app --host 0.0.0.0 --port 8000"]
