"""Base parser interface."""

from abc import ABC, abstractmethod
from typing import TextIO

from logforge.domain.log_entry import LogEntry


class BaseParser(ABC):
    """Abstract parser interface."""

    @abstractmethod
    def parse(self, stream: TextIO) -> list[LogEntry]:
        """Parse a text stream into log entries."""