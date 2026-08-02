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
                parts = line.split(maxsplit=4)

                if len(parts) != 5:
                    raise ParsingError(
                        f"Invalid log entry at line {line_number}"
                    )

                timestamp = datetime.fromisoformat(
                    f"{parts[0]} {parts[1]}"
                )

                level = LogLevel(parts[2])
                service = parts[3]
                message = parts[4]

                entries.append(
                    LogEntry(
                        timestamp=timestamp,
                        level=level,
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