"""Use case for log analysis."""

from pathlib import Path

from logforge.application.context import ApplicationContext
from logforge.domain.analysis_report import AnalysisReport


class AnalyzeLogUseCase:
    """Analyze a single log file."""

    def __init__(self, context: ApplicationContext) -> None:
        """Initialize the use case."""

        self._context = context

    def execute(
        self,
        path: Path,
    ) -> AnalysisReport:
        """Analyze the specified log file."""

        parser = self._context.parser_registry.get(path)

        with self._context.file_loader.open(path) as stream:
            entries = parser.parse(stream)

        return self._context.analysis_service.analyze(entries)