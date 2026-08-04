"""CLI application."""

import typer

from logforge.cli.commands import analyze

app = typer.Typer(
    help="LogForge - Enterprise log analysis toolkit.",
)

app.command()(analyze)