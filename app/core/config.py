from pydantic_settings import BaseSettings, SettingsConfigDict

# BaseSettings para cargar variables de entorno desde un archivo .env
# lee datos de variables de entorno y los convierte en atributos de la clase Settings,
# lo que facilita la gestión de la configuración de la aplicación.


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    DATABASE_URL: str
    SECRET_KEY: str
    ENV: str = "development"
    PORT: int = 8000


settings = Settings()
# patron Singleton para que la configuración se cargue una sola vez y
# se pueda usar en toda la aplicación importando esta instancia de settings.
