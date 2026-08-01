"""Tests for application bootstrap."""

from logforge.bootstrap import bootstrap
from logforge.config.settings import Settings


def test_bootstrap_returns_settings() -> None:
    """Verify that bootstrap returns validated settings."""

    settings = bootstrap()

    assert isinstance(settings, Settings)


def test_bootstrap_loads_application_name() -> None:
    """Verify that application settings are loaded."""

    settings = bootstrap()

    assert settings.application.name == "logforge"


def test_bootstrap_loads_environment() -> None:
    """Verify that application environment is loaded."""

    settings = bootstrap()

    assert settings.application.environment == "development"