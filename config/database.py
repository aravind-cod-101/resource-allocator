from .settings import settings

DATABASE_URL=f"{settings.DB_TYPE}://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
