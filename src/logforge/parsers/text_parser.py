"""Plain text parser."""

from datetime import datetime
from pathlib import Path
from typing import TextIO

from logforge.domain.enums import LogLevel
from logforge.domain.log_entry import LogEntry
from logforge.parsers.base import BaseParser
from logforge.parsers.exceptions import ParsingError


class PlainTextParser(BaseParser):
    """Parser for plain text log files."""

    def parse(self, stream: TextIO) -> list[LogEntry]:
        """Parse plain text log entries."""

        entries: list[LogEntry] = []

        for line_number, line in enumerate(stream, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                timestamp_str, level, service, message = line.split(
                    maxsplit=4,
                )

                timestamp = datetime.fromisoformat(timestamp_str)

                entries.append(
                    LogEntry(
                        timestamp=timestamp,
                        level=LogLevel(level),
                        service=service,
                        message=message,
                        source=Path("<stream>"),
                        line_number=line_number,
                    )
                )

            except Exception as error:
                raise ParsingError(
                    f"Invalid log entry at line {line_number}"
                ) from error

        return entries