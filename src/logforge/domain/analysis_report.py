"""Domain model representing log analysis results."""

from dataclasses import dataclass


@dataclass(slots=True)
class AnalysisReport:
    """Summary of log analysis."""

    total_entries: int
    debug_entries: int
    info_entries: int
    warning_entries: int
    error_entries: int
    critical_entries: int