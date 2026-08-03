"""Tests for the default line parser."""

from datetime import datetime

import pytest

from logforge.domain.enums import LogLevel
from logforge.parsers.exceptions import ParsingError
from logforge.parsers.line_parsers.default import DefaultLineParser


def test_parse_valid_log_line() -> None:
    """Verify that a valid log line is parsed correctly."""

    parser = DefaultLineParser()

    entry = parser.parse(
        line=(
            "2026-08-02 10:17:11 "
            "ERROR payment-service Database timeout"
        ),
        line_number=1,
    )

    assert entry.timestamp == datetime(
        2026,
        8,
        2,
        10,
        17,
        11,
    )
    assert entry.level is LogLevel.ERROR
    assert entry.service == "payment-service"
    assert entry.message == "Database timeout"
    assert entry.line_number == 1


def test_invalid_log_line_raises_exception() -> None:
    """Verify that an invalid log line raises ParsingError."""

    parser = DefaultLineParser()

    with pytest.raises(ParsingError):
        parser.parse(
            line="invalid log line",
            line_number=1,
        )


def test_invalid_log_level_raises_exception() -> None:
    """Verify that an unknown log level raises ParsingError."""

    parser = DefaultLineParser()

    with pytest.raises(ParsingError):
        parser.parse(
            line=(
                "2026-08-02 10:17:11 "
                "INVALID payment-service Message"
            ),
            line_number=1,
        )