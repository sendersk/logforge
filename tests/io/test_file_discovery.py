"""Tests for log file discovery."""

from pathlib import Path

from logforge.io.file_discovery import LogFileDiscovery


def test_discover_single_log_file(tmp_path: Path) -> None:
    """Verify discovery of a single log file."""

    log_file = tmp_path / "application.log"
    log_file.touch()

    discovery = LogFileDiscovery()

    result = discovery.discover(log_file)

    assert result == [log_file]


def test_ignore_non_log_file(tmp_path: Path) -> None:
    """Verify that non-log files are ignored."""

    text_file = tmp_path / "application.txt"
    text_file.touch()

    discovery = LogFileDiscovery()

    result = discovery.discover(text_file)

    assert result == []


def test_discover_log_files_from_directory(tmp_path: Path) -> None:
    """Verify discovery of log files from a directory."""

    first_log = tmp_path / "application.log"
    second_log = tmp_path / "database.log"
    ignored_file = tmp_path / "notes.txt"

    first_log.touch()
    second_log.touch()
    ignored_file.touch()

    discovery = LogFileDiscovery()

    result = discovery.discover(tmp_path)

    assert result == sorted([first_log, second_log])


def test_discover_only_top_level_files(tmp_path: Path) -> None:
    """Verify that non-recursive discovery ignores nested directories."""

    top_level_log = tmp_path / "application.log"
    nested_directory = tmp_path / "archive"
    nested_log = nested_directory / "old.log"

    top_level_log.touch()
    nested_directory.mkdir()
    nested_log.touch()

    discovery = LogFileDiscovery()

    result = discovery.discover(tmp_path)

    assert result == [top_level_log]


def test_discover_files_recursively(tmp_path: Path) -> None:
    """Verify recursive discovery of log files."""

    top_level_log = tmp_path / "application.log"
    nested_directory = tmp_path / "archive"
    nested_log = nested_directory / "old.log"

    top_level_log.touch()
    nested_directory.mkdir()
    nested_log.touch()

    discovery = LogFileDiscovery()

    result = discovery.discover(
        tmp_path,
        recursive=True,
    )

    assert result == sorted([top_level_log, nested_log])


def test_discover_nonexistent_path(tmp_path: Path) -> None:
    """Verify that a nonexistent path returns no files."""

    missing_path = tmp_path / "missing"

    discovery = LogFileDiscovery()

    result = discovery.discover(missing_path)

    assert result == []


def test_discovery_is_case_insensitive(tmp_path: Path) -> None:
    """Verify case-insensitive log file discovery."""

    log_file = tmp_path / "APPLICATION.LOG"
    log_file.touch()

    discovery = LogFileDiscovery()

    result = discovery.discover(log_file)

    assert result == [log_file]