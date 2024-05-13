import reflex as rx
from ..styles.styles import (
    SIZE,
    EM_SIZE,
    MAX_WIDTH,
    IMAGE_HEIGHT
)

from ..views.links import links
from ..components.heading import heading


def footer() -> rx.Component:
    return rx.hstack(
        links(),        
        padding=EM_SIZE.SMALL,
        spacing=SIZE.SMALL
    )

