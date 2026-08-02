"""Base parser interface."""

from abc import ABC, abstractmethod
from pathlib import Path

from logforge.domain.log_entry import LogEntry


class BaseParser(ABC):
    """Abstract parser interface."""

    @abstractmethod
    def parse(self, path: Path) -> list[LogEntry]:
        """Parse a file into domain log entries."""