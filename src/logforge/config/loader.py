"""Configuration loading utilities."""

from pathlib import Path

import yaml
from pydantic import ValidationError

from logforge.config.exceptions import ConfigurationError
from logforge.config.settings import Settings


def load_config(path: Path) -> Settings:
    """
    Load application configuration from YAML file.

    Args:
        path: Path to YAML configuration file.

    Returns:
        Validated application settings.

    Raises:
        ConfigurationError:
            If the configuration file is missing, invalid,
            or cannot be parsed.
    """

    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return Settings.model_validate(data)

    except FileNotFoundError as error:
        raise ConfigurationError(
            f"Configuration file not found: {path}"
        ) from error

    except yaml.YAMLError as error:
        raise ConfigurationError(
            f"Invalid YAML configuration: {path}"
        ) from error

    except ValidationError as error:
        raise ConfigurationError(
            "Configuration validation failed."
        ) from error