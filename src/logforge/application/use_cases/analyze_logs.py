"""Use cases for log analysis."""

from pathlib import Path

from logforge.application.context import ApplicationContext
from logforge.domain.analysis_report import AnalysisReport


class AnalyzeLogUseCase:
    """Analyze one or more log files."""

    def __init__(self, context: ApplicationContext) -> None:
        """Initialize the use case."""

        self._context = context

    def execute(
        self,
        path: Path,
    ) -> AnalysisReport:
        """Analyze a file or directory."""

        files = self._context.file_discovery.discover(
            path,
            recursive=True,
        )

        report = AnalysisReport()

        for file_path in files:
            file_report = self._analyze_file(file_path)
            report = report.merge(file_report)

        return report

    def _analyze_file(self, path: Path) -> AnalysisReport:
        """Analyze a single log file."""

        parser = self._context.parser_registry.get(path)

        with self._context.file_loader.open(path) as stream:
            entries = parser.parse(stream)

        return self._context.analysis_service.analyze(entries)