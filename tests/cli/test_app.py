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

    assert result.exit_code == 0, (
        f"\nstdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}\n"
        f"exception:{result.exception}"
    )


def test_analyze_directory(tmp_path: Path) -> None:
    """Verify that the CLI can analyze a directory."""

    first_log = tmp_path / "first.log"
    second_log = tmp_path / "second.log"

    first_log.write_text(
        "2026-08-02 10:17:11 INFO app Started\n",
        encoding="utf-8",
    )

    second_log.write_text(
        "2026-08-02 10:18:11 ERROR api Failed\n",
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        ["analyze", str(tmp_path)],
    )

    assert result.exit_code == 0, (
        f"\nstdout: \n{result.stdout}\n"
        f"stderr:\n{result.stderr}\n"
        f"exception:{result.exception}"
    )

    assert "Log Analysis Summary" in result.stdout
    assert "Total entries : 2" in result.stdout
    assert "INFO          : 1" in result.stdout
    assert "ERROR         : 1" in result.stdout


def test_analyze_empty_directory(tmp_path: Path) -> None:
    """Verify that the CLI handles an empty directory."""

    result = runner.invoke(
        app,
        ["analyze", str(tmp_path)],
    )

    assert result.exit_code == 0, (
        f"\nstdout:\n{result.stdout}"
        f"stderr:\n{result.stderr}"
        f"exception:{result.exception}"
    )

    assert "Log Analysis Summary" in result.stdout
    assert "Total entries : 0" in result.stdout