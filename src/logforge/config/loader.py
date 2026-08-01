"""Configuration loading utilities."""

from pathlib import Path

import yaml

from logforge.config.settings import Settings


def load_config(path: Path) -> Settings:
    """
    Load application configuration from YAML file.

    Args:
        path: Path to YAML configuration file.

    Returns:
        Validated application settings.
    """

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return Settings.model_validate(data)