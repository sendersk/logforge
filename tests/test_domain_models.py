"""Tests for domain models."""

from datetime import datetime
from pathlib import Path

from logforge.domain.analysis_report import AnalysisReport
from logforge.domain.enums import LogLevel
from logforge.domain.log_entry import LogEntry


def test_log_entry_creation() -> None:
    """Verify LogEntry creation."""

    entry = LogEntry(
        timestamp=datetime(2026, 1, 1, 12, 0, 0,),
        level=LogLevel.ERROR,
        service="payment-api",
        message="Connection timeout",
        source=Path("logs/app.log"),
        line_number=42,
    )

    assert entry.level is LogLevel.ERROR
    assert entry.service == "payment-api"
    assert entry.line_number == 42


def test_analysis_report_creation() -> None:
    """Verify AnalysisReport creation."""

    report = AnalysisReport(
        total_entries=100,
        debug_entries=20,
        info_entries=40,
        warning_entries=15,
        error_entries=20,
        critical_entries=5,
    )

    assert report.total_entries == 100
    assert report.error_entries == 20
    assert report.critical_entries == 5