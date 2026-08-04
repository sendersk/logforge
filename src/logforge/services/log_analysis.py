"""Log analysis service."""

from logforge.domain.analysis_report import AnalysisReport
from logforge.domain.enums import LogLevel
from logforge.domain.log_entry import LogEntry


class LogAnalysisService:
    """Analyze parsed log entries."""

    def analyze(
        self,
        entries: list[LogEntry],
    ) -> AnalysisReport:
        """Generate an analysis report."""

        report = AnalysisReport(
            total_entries=len(entries),
            debug_entries=0,
            info_entries=0,
            warning_entries=0,
            error_entries=0,
            critical_entries=0,
        )

        for entry in entries:
            match entry.level:
                case LogLevel.DEBUG:
                    report.debug_entries += 1

                case LogLevel.INFO:
                    report.info_entries += 1

                case LogLevel.WARNING:
                    report.warning_entries += 1

                case LogLevel.ERROR:
                    report.error_entries += 1

                case LogLevel.CRITICAL:
                    report.critical_entries += 1

        return report