from pydantic_settings import BaseSettings
from pydantic import Field, ValidationError

class Settings(BaseSettings):
    DB_HOST: str = Field(..., description="Database host")
    DB_PORT: int = Field(..., description="Database port")
    DB_USER: str = Field(..., description="Database user")
    DB_PASSWORD: str = Field(..., description="Database password")
    DB_NAME: str = Field(..., description="Database name")
    DB_TYPE: str = Field(..., description="Database type")
    API_KEY: str = Field(..., description="API KEY")

    class Config:
        env_file = ".env"
        case_sensitive = True

try:
    settings = Settings() # type: ignore
except ValidationError as e:
    # Fail FAST if env vars are missing or invalid
    raise RuntimeError(
        f"Validation error on environment variables: {e}"
    )