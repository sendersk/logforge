"""Smoke tests for the CLI."""

from typer.testing import CliRunner

from logforge.cli.app import app

runner = CliRunner()


def test_cli_runs() -> None:
    """Verify that the CLI starts."""

    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Usage:" in result.stdout


def test_analyze_command() -> None:
    """Verify that the 'analyze' command is available."""

    result = runner.invoke(
        app,
        ["analyze", "sample.log"],
    )

    assert result.exit_code == 0