import reflex as rx
from ..styles.styles import (
    SIZE,
    EM_SIZE,
    MAX_WIDTH,
    IMAGE_HEIGHT
)

def heading(text: str, h1=False) -> rx.Component:
    return rx.heading(
        text,
        as_="h1" if h1 else "h2",
        size=SIZE.BIG if h1 else SIZE.MEDIUM
    )