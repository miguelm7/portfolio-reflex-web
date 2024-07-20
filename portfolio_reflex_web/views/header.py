import reflex as rx
from ..styles.styles import (
    SIZE,
    EM_SIZE,
    MAX_WIDTH,
    IMAGE_HEIGHT
)

from ..views.links import links
from ..components.heading import heading


def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src="avatar.jpeg",
            fallback="MM",
            size=SIZE.BIG,
            radius="full"
        ),
        rx.vstack(
            heading("Miguel Moreno Rodríguez",True),
            heading("Data Scientist | Python Developer"),
            rx.text(
                rx.icon("map-pin"),
                "Alicante",
                display="inherit"
            ),
            links(),
            spacing=SIZE.SMALL
        ),
        padding=EM_SIZE.SMALL,
        spacing=SIZE.SMALL
    )

