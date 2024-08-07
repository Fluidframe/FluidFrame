from typing import Optional
from fluidframe.core import span, div


def with_tooltip(content: str, message: str, cls: str) -> str:
    return div(
        content,
        span(message, cls=f"tooltip-content {cls}"),
        cls="inline-block tooltip-trigger"
    )