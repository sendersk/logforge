"""Base interface for line parsers."""

from abc import ABC, abstractmethod

from logforge.domain.log_entry import LogEntry


class BaseLineParser(ABC):
    """Parse a single log line."""

    @abstractmethod
    def parse(
            self,
            line: str,
            line_number: int,
    ) -> LogEntry:
        """Convert a line into a LogEntry."""