"""Default parser for plain text log entries."""

from datetime import datetime
from pathlib import Path

from logforge.domain.enums import LogLevel
from logforge.domain.log_entry import LogEntry
from logforge.parsers.exceptions import ParsingError
from logforge.parsers.line_parsers.base import BaseLineParser


class DefaultLineParser(BaseLineParser):
    """Parse a single plain text log entry."""

    def parse(
            self,
            line: str,
            line_number: int,
    ) -> LogEntry:
        """Convert a log line into a LogEntry."""

        try:
            parts = line.split(maxsplit=4)

            if len(parts) != 5:
                raise ParsingError(
                    f"Invalid log entry at line {line_number}"
                )

            timestamp = datetime.fromisoformat(
                f"{parts[0]} {parts[1]}"
            )

            return LogEntry(
                timestamp=timestamp,
                level=LogLevel(parts[2]),
                service=parts[3],
                message=parts[4],
                source=Path("<stream>"),
                line_number=line_number,
            )

        except ValueError as error:
            raise ParsingError(
                f"Invalid log entry at line {line_number}"
            ) from error