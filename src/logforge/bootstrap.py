"""Application bootstrap."""

import logging
from pathlib import Path

from logforge.application.context import ApplicationContext
from logforge.config.loader import load_config
from logforge.io.file_loader import FileLoader
from logforge.logging.setup import configure_logging
from logforge.parsers.registry import ParserRegistry
from logforge.parsers.text_parser import PlainTextParser
from logforge.services.log_analysis import LogAnalysisService

CONFIG_PATH = Path("config/app.yaml")


def bootstrap() -> ApplicationContext:
    """Initialize application dependencies."""

    settings = load_config(CONFIG_PATH)

    configure_logging()

    logger = logging.getLogger(__name__)

    logger.info(
        "Application '%s' started in %s mode.",
        settings.application.name,
        settings.application.environment,
    )

    parser_registry = ParserRegistry()
    parser_registry.register(".log", PlainTextParser())

    return ApplicationContext(
        settings=settings,
        file_loader=FileLoader(),
        parser_registry=parser_registry,
        analysis_service=LogAnalysisService(),
    )