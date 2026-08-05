"""CLI application."""

import typer

from logforge.cli import commands


app = typer.Typer(
    name="logforge",
    help="Enterprise log analysis toolkit.",
    no_args_is_help=True,
)

app.command(name="analyze")(commands.analyze)