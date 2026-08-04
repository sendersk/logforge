"""Application entry point for LogForge."""

from logforge.bootstrap import bootstrap
from logforge.cli.app import app


def main() -> None:
    """Initialize the application and start the CLI."""

    bootstrap()
    app()


if __name__ == "__main__":
    main()