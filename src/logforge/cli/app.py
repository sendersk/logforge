"""CLI application."""

import typer

from logforge.cli.commands import analyze

app = typer.Typer(
    name="logforge",
    help="Enterprise log analysis toolkit.",
    no_args_is_help=True,
)

app.command("analyze")(analyze)