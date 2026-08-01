"""Application entry point for LogForge."""

import logging

from logforge.logging.setup import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the LogForge application."""

    configure_logging()

    logger.info("LogForge application started")


if __name__ == "__main__":
    main()