"""Smoke tests for the CLI."""

from pathlib import Path
from typer.testing import CliRunner

from logforge.cli.app import app

runner = CliRunner()


def test_cli_runs() -> None:
    """Verify that the CLI starts."""

    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Usage:" in result.stdout


def test_analyze_command(tmp_path: Path) ->None:
    """Verify analyze command."""

    log_file = tmp_path / "sample.log"

    log_file.write_text(
        "2026-08-02 10:17:11 INFO app Started\n",
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        ["analyze", str(log_file)],
    )

    assert result.exit_code == 0