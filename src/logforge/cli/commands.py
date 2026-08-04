"""CLI commands."""

from pathlib import Path

import typer


def analyze(path: Path) -> None:
    """Analyze a log file."""

    typer.echo(f"Analyzing {path}")