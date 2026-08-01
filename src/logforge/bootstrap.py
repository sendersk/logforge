"""Application bootstrap."""

from pathlib import Path

from logforge.config.loader import load_config
from logforge.logging.setup import configure_logging


CONFIG_PATH = Path("config/app.yaml")


def bootstrap():
    """Initialize application dependencies."""

    settings = load_config(CONFIG_PATH)

    configure_logging()

    return settings