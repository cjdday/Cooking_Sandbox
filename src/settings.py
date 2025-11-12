# settings.py
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    app_env: str = os.getenv("APP_ENV", "dev")  # dev | uat | prod
    host: str = os.getenv("HOST", "0.0.0.0")  # container binds to 0.0.0.0
    port: int = int(os.getenv("PORT", "8000"))
    # Comma-separated CORS list: "http://localhost:3000,https://yourdomain.com"
    allow_origins_csv: str = os.getenv("ALLOW_ORIGINS", "http://localhost:3000")

    @property
    def allow_origins(self) -> List[AnyHttpUrl] | List[str]:
        return [o.strip() for o in self.allow_origins_csv.split(",") if o.strip()]


settings = Settings()
