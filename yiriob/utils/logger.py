import logging

try:
    import rich
    from rich.logging import RichHandler

    pprint = rich.print
except ImportError:
    RichHandler = None
    pprint = print


logging.basicConfig(
    level=logging.DEBUG,
    handlers=[RichHandler()] if RichHandler is not None else [],
)

logger = logging.getLogger("yiri-bot")

__all__ = ["logger", "pprint"]
