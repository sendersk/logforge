"""Application configuration domain."""

from pydantic import BaseModel


class ApplicationSettings(BaseModel):
    """Application metadata configuration."""

    name: str
    environment: str


class LoggingSettings(BaseModel):
    """Logging configuration."""

    level: str


class Settings(BaseModel):
    """Root application configuration."""

    application: ApplicationSettings
    logging: LoggingSettings