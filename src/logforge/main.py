"""Application entry point for LogForge."""

import logging

from logforge.bootstrap import bootstrap

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the LogForge application."""

    settings = bootstrap()

    logger.info(
        "Application '%s' started in %s mode.",
        settings.application.name,
        settings.application.environment,
    )


if __name__ == "__main__":
    main()