"""Log file discovery utilities."""

from pathlib import Path


class LogFileDiscovery:
    """Discover log files from files and directories."""

    def __init__(self, extension: str = ".log") -> None:
        """Initialize the log file discovery service."""

        self._extension = extension.lower()

    def discover(
        self,
        path: Path,
        recursive: bool = False,
    ) -> list[Path]:
        """Discover log files from the given path."""

        if path.is_file():
            return self._discover_file(path)

        if path.is_dir():
            return self._discover_directory(path, recursive)

        return []

    def _discover_file(self, path: Path) -> list[Path]:
        """Return the file if it has the expected extension."""

        if path.suffix.lower() == self._extension:
            return [path]

        return []

    def _discover_directory(
        self,
        path: Path,
        recursive: bool,
    ) -> list[Path]:
        """Discover log files in a directory."""

        pattern = f"*{self._extension}"

        if recursive:
            files = path.rglob(pattern)
        else:
            files = path.glob(pattern)

        return sorted(
            file
            for file in files
            if file.is_file()
        )