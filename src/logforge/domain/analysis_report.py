"""Log analysis report."""

from dataclasses import dataclass


@dataclass()
class AnalysisReport:
    """Summary of analyzed log entries."""

    total_entries: int = 0
    debug_entries: int = 0
    info_entries: int = 0
    warning_entries: int = 0
    error_entries: int = 0
    critical_entries: int = 0

    def merge(self, other: "AnalysisReport") -> "AnalysisReport":
        """Merge another analysis report into this report."""

        return AnalysisReport(
            total_entries=self.total_entries + other.total_entries,
            debug_entries=self.debug_entries + other.debug_entries,
            info_entries=self.info_entries + other.info_entries,
            warning_entries=self.warning_entries + other.warning_entries,
            error_entries=self.error_entries + other.error_entries,
            critical_entries=self.critical_entries + other.critical_entries
        )