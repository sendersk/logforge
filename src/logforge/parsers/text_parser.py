"""Plain text parser."""

from pathlib import Path

from logforge.domain.log_entry import LogEntry
from logforge.parsers.base import BaseParser


class PlainTextParser(BaseParser):
    """Parser for plain text log files."""

    def parse(self, path: Path) -> list[LogEntry]:
        """Parse plain text log file."""

        raise NotImplementedError