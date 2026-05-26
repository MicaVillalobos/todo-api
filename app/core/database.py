# Solo maneja configuración de base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings


# Base de la que heredan todos los modelos
# Equivalente a @Entity en JPA
class Base(DeclarativeBase):
    pass


engine = create_engine(settings.DATABASE_URL)
# crea la conexión a la base de datos usando la URL definida en las variables de entorno

SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Crea una clase de sesión local que se usará para interactuar con la base de datos.
# autocommit=False para que los cambios no se guarden automáticamente
# autoflush=False para evitar que se envíen cambios a la base de datos antes de tiempo,
# no sincroniza automáticamente los cambios con la base de datos hasta que se llame a commit() explícitamente
# y bind=engine para asociar esta sesión con el motor de la base de datos que creamos.
# Cada vez que llamamos a sessionLocal crea una nueva sesión de base de datos.


def get_db():
    db: Session = SesionLocal()
    try:
        yield db
    finally:
        db.close()


# con yield la sesion siempre se cierra después de usarla,
# incluso si ocurre un error, lo que evita fugas de conexiones a la base de datos.
# con finally db.close() se asegura que la sesión se cierre correctamente después de su uso,
# lo que es crucial para liberar recursos y evitar problemas de rendimiento o bloqueos en la base.
