from rxconfig import config
import reflex as rx
from .views.header import header
from .views.footer import footer
from .styles.styles import (
    SIZE,
    EM_SIZE,
    MAX_WIDTH,
    IMAGE_HEIGHT,
    STYLESHEETS,
    BASE_STYLE
)

from .components.heading import heading


# class State(rx.State):
#     """The app state."""


def index() -> rx.Component:
    return rx.center(
            rx.vstack(
            header(),
            heading("Sobre mí"),
            rx.text(
                """
                Data Scientist con más de 3 años de experiencia en el desarrollo de soluciones de analítica de datos,
                ingeniería de datos y Machine Learning. Experiencia en la creación de procesos ETL, desarrollo y
                mantenimiento de modelos de aprendizaje automático, desarrollo de APIs, análisis exploratorio y
                visualización de datos. Analítico y creativo en la resolución de problemas.
                """
                ),
            rx.divider(),
            rx.text("Tecnologias"),
            rx.text("Experiencia"),
            rx.text("Proyectos"),
            rx.text("Formación"),
            rx.text("Extra"),
            rx.divider(),
            footer(),
            # end
            max_width=MAX_WIDTH,
            padding=EM_SIZE.SMALL,
            width="100%"
        )
    )


app = rx.App(
    # stylesheets=STYLESHEETS,
    # style=BASE_STYLE,
    theme=rx.theme(
        appearance="light",
        accent_color="gray",
        radius="full"
    )
)
app.add_page(index)
