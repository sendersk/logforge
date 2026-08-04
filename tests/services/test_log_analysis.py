"""Tests for log analysis service."""

from datetime import datetime
from pathlib import Path

from logforge.domain.analysis_report import AnalysisReport
from logforge.domain.enums import LogLevel
from logforge.domain.log_entry import LogEntry
from logforge.services.log_analysis import LogAnalysisService


def create_entry(level: LogLevel) -> LogEntry:
    """Create a sample log entry."""

    return LogEntry(
        timestamp=datetime.now(),
        level=level,
        service="payment-service",
        message="Sample message",
        source=Path("sample.log"),
        line_number=1,
    )


def test_generate_report() -> None:
    """Verify report generation."""

    entries = [
        create_entry(LogLevel.INFO),
        create_entry(LogLevel.INFO),
        create_entry(LogLevel.WARNING),
        create_entry(LogLevel.ERROR),
        create_entry(LogLevel.ERROR),
        create_entry(LogLevel.CRITICAL),
    ]

    service = LogAnalysisService()

    report = service.analyze(entries)

    assert isinstance(report, AnalysisReport)

    assert report.total_entries == 6
    assert report.info_entries == 2
    assert report.warning_entries == 1
    assert report.error_entries == 2
    assert report.critical_entries == 1
    assert report.debug_entries == 0