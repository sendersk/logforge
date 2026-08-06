"""CLI commands."""

import typer

from pathlib import Path
from typing import Annotated


from logforge.application.use_cases.analyze_logs import AnalyzeLogUseCase
from logforge.bootstrap import bootstrap


def analyze(
        path: Annotated[
            Path,
            typer.Argument(
                exists=True,
                file_okay=True,
                dir_okay=False,
                readable=True,
                resolve_path=True,
                help="Path to the log file."
            ),
        ],
) -> None:
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