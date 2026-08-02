"""Parser exceptions."""


class ParserError(Exception):
    """Base parser exception."""


class UnsupportedFileTypeError(ParserError):
    """Raised when no parser supports the requested file."""


class ParsingError(ParserError):
    """Raised when parsing fails."""