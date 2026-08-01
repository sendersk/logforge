"""Tests for configuration handling."""

from pathlib import Path

from logforge.config.loader import load_config


def test_load_config() -> None:
    """Verify configuration loading."""

    config_path = Path("config/app.yaml")

    settings = load_config(config_path)

    assert settings.application.name == "logforge"
    assert settings.logging.level == "INFO"