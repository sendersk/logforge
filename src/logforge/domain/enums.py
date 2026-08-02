"""Domain enumerations."""

from enum import StrEnum


class LogLevel(StrEnum):
    """Supported log severity levels."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"