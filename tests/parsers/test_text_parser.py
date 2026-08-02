from io import StringIO

from logforge.domain.enums import LogLevel
from logforge.parsers.text_parser import PlainTextParser


def test_parse_single_log_entry() -> None:
    parser = PlainTextParser()

    stream = StringIO(
        "2026-08-02 10:17:11 ERROR payment-service Database timeout\n"
    )

    entries = parser.parse(stream)

    assert len(entries) == 1

    entry = entries[0]

    assert entry.level is LogLevel.ERROR
    assert entry.service == "payment-service"
    assert entry.message == "Database timeout"