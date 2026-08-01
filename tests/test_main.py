"""Tests for application entry point."""

import logging

from logforge.main import main


def test_application_starts(caplog) -> None:
    """Verify that application startup is logged."""
    caplog.set_level(logging.INFO)

    main()

    assert "Application 'logforge' started in development mode." in caplog.text