"""Domain model representing a single log entry."""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from logforge.domain.enums import LogLevel


@dataclass(slots=True, frozen=True)
class LogEntry:
    """Represents a parsed log entry."""

    timestamp: datetime
    level: LogLevel
    service: str
    message: str
    source: Path
    line_number: int