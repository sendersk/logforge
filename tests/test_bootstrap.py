"""Tests for application bootstrap."""

from logforge.application.context import ApplicationContext
from logforge.bootstrap import bootstrap


def test_bootstrap_returns_application_context() -> None:
    """Verify that bootstrap returns an application context."""

    context = bootstrap()

    assert isinstance(context, ApplicationContext)


def test_bootstrap_loads_application_name() -> None:
    """Verify application name."""

    context = bootstrap()

    assert context.settings.application.name == "logforge"


def test_bootstrap_loads_environment() -> None:
    """Verify environment."""

    context = bootstrap()

    assert context.settings.application.environment == "development"