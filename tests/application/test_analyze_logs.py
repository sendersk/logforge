"""Tests for AnalyzeLogUseCase."""

from pathlib import Path

from logforge.application.use_cases.analyze_logs import AnalyzeLogUseCase
from logforge.bootstrap import bootstrap


def test_analyze_log_file(tmp_path: Path) -> None:
    """Verify that a log file can be analyzed."""

    log_file = tmp_path / "application.log"

    log_file.write_text(
        (
            "2026-08-02 10:17:11 INFO app Started\n"
            "2026-08-02 10:17:12 ERROR app Database timeout\n"
            "2026-08-02 10:17:13 WARNING app Retry\n"
        ),
        encoding="utf-8",
    )

    context = bootstrap()

    report = AnalyzeLogUseCase(context).execute(log_file)

    assert report.total_entries == 3
    assert report.info_entries == 1
    assert report.warning_entries == 1
    assert report.error_entries == 1
    assert report.critical_entries == 0


def test_analyze_multiple_log_files(tmp_path: Path) -> None:
    """Verify that multiple log files are analyzed together."""

    first_log = tmp_path / "first.log"
    second_log = tmp_path / "second.log"

    first_log.write_text(
        "2026-08-02 10:17:11 INFO app Started\n"
        "2026-08-02 10:18:11 ERROR app Failed\n",
        encoding="utf-8",
    )

    second_log.write_text(
        "2026-08-02 10:19:11 WARNING api Slow response\n"
        "2026-08-02 10:20:11 INFO api Recovered\n",
        encoding="utf-8",
    )

    context = bootstrap()
    use_case = AnalyzeLogUseCase(context)

    report = use_case.execute(tmp_path)

    assert report.total_entries == 4
    assert report.info_entries == 2
    assert report.warning_entries == 1
    assert report.error_entries == 1