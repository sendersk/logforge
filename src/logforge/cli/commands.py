"""CLI commands."""

from pathlib import Path

import typer

from logforge.application.use_cases.analyze_logs import AnalyzeLogUseCase
from logforge.bootstrap import bootstrap


def analyze(path: Path) -> None:
    """Analyze a log file."""

    context = bootstrap()

    report = AnalyzeLogUseCase(context).execute(path)

    typer.echo()
    typer.echo("Log Analysis Summary")
    typer.echo("=" * 32)
    typer.echo(f"Total entries : {report.total_entries}")
    typer.echo(f"DEBUG         : {report.debug_entries}")
    typer.echo(f"INFO          : {report.info_entries}")
    typer.echo(f"WARNING       : {report.warning_entries}")
    typer.echo(f"ERROR         : {report.error_entries}")
    typer.echo(f"CRITICAL      : {report.critical_entries}")