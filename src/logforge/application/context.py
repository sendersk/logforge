"""Application context."""

from dataclasses import dataclass

from logforge.config.settings import Settings
from logforge.io.file_loader import FileLoader
from logforge.parsers.registry import ParserRegistry
from logforge.services.log_analysis import LogAnalysisService


@dataclass(slots=True)
class ApplicationContext:
    """Container for application services."""

    settings: Settings
    file_loader: FileLoader
    parser_registry: ParserRegistry
    analysis_service: LogAnalysisService