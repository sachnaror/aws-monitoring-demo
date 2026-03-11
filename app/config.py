from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "AWS Monitoring Demo"
    APP_ENV: str = "development"
    APP_PORT: int = 8000

    LOG_LEVEL: str = "INFO"
    ALERT_EMAIL: str = "alerts@example.com"

    CHECK_INTERVAL: int = 10
    LATENCY_THRESHOLD: int = 2

class Config:
    env_file = ".env"


settings = Settings()
