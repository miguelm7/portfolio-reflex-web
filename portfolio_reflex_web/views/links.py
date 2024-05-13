import reflex as rx
from ..components.link_icon import link_icon

from ..styles.styles import (
    SIZE,
    EM_SIZE,
    MAX_WIDTH,
    IMAGE_HEIGHT
)


def links() -> rx.Component:
    return rx.flex(
        link_icon(
            "mail",
            f"mailto:miguelmore100@gmail.com",
            "miguelmore100@gmail.com",
            True
        ),
        rx.hstack(
            link_icon(
                "file-text",
                "CV MIGUEL (ES).pdf"
            ),
            link_icon(
                "github",
                "https://github.com/miguelm7"
            ),
            link_icon(
                "linkedin",
                "http://www.linkedin.com/in/miguel-moreno-rodr%C3%ADguez-0164a5123"
            ),
            spacing=SIZE.SMALL
        ),
        spacing=SIZE.SMALL,
        flex_direction=["column", "column", "row"]
    )