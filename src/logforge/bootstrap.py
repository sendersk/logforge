"""Application bootstrap."""

import logging
from pathlib import Path

from logforge.application.context import ApplicationContext
from logforge.config.loader import load_config
from logforge.config.settings import Settings
from logforge.io.file_discovery import LogFileDiscovery
from logforge.io.file_loader import FileLoader
from logforge.logging.setup import configure_logging
from logforge.parsers.registry import ParserRegistry
from logforge.parsers.text_parser import PlainTextParser
from logforge.services.log_analysis import LogAnalysisService

CONFIG_PATH = Path("config/app.yaml")


def bootstrap() -> ApplicationContext:
    """Initialize application dependencies."""

    settings: Settings = load_config(CONFIG_PATH)

    configure_logging()

    parser_registry = ParserRegistry()
    parser_registry.register(".log", PlainTextParser())

    context = ApplicationContext(
        settings=settings,
        file_loader=FileLoader(),
        file_discovery=LogFileDiscovery(),
        parser_registry=parser_registry,
        analysis_service=LogAnalysisService(),
    )

    logger = logging.getLogger(__name__)

    logger.info(
        "Application '%s' started in %s mode.",
        settings.application.name,
        settings.application.environment,
    )

    return context