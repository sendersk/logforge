"""Logging configuration for LogForge application."""

import logging
import sys

DEFAULT_LOG_FORMAT = (
"%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

DEFAULT_LOG_LEVEL = logging.INFO


def configure_logging() -> None:
    """
    Configure application-wide logging.

    Sets the root logger configuration used by all
    LogForge modules.
    """

    logging.basicConfig(
        level=DEFAULT_LOG_LEVEL,
        format=DEFAULT_LOG_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ],
    )