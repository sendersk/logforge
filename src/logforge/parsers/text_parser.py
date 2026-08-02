"""Plain text log parser."""

from typing import TextIO

from logforge.domain.log_entry import LogEntry
from logforge.parsers.base import BaseParser
from logforge.parsers.line_parsers.default import DefaultLineParser


class PlainTextParser(BaseParser):
    """Parser for plain text log files."""

    def __init__(self) -> None:
        """Initialize the parser."""

        self._line_parser = DefaultLineParser()

    def parse(self, stream: TextIO) -> list[LogEntry]:
        """Parse plain text log entries."""

        entries: list[LogEntry] = []

        for line_number, line in enumerate(stream, start=1):
            line = line.strip()

            if not line:
                continue

            entry = self._line_parser.parse(
                line=line,
                line_number=line_number,
            )

            entries.append(entry)

        return entries