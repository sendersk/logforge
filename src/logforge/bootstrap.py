"""Application bootstrap."""

import logging
from pathlib import Path

from logforge.config.loader import load_config
from logforge.logging.setup import configure_logging

CONFIG_PATH = Path("config/app.yaml")


def bootstrap():
    """Initialize application dependencies."""

    settings = load_config(CONFIG_PATH)

    configure_logging()

    logger = logging.getLogger(__name__)

    logger.info(
        "Application '%s' started in %s mode.",
        settings.application.name,
        settings.application.environment,
    )

    return settings