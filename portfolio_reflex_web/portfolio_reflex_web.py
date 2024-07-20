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
from .components.skills_grid import skills_grid
from .components.experience_grid import experience_grid
from .components.project_grid import project_grid

G_TAG = "G-W0XSPLQDLS"


# class State(rx.State):
#     """The app state."""

academic = [
        {
            "position": "MSc Intelligent Vision - University of Lincoln, UK",
            "dates": "Sep 2019 - Ago 2020",
            "description_points": [
                "Developed and maintained web applications.",
                "Collaborated with cross-functional teams.",
                "Implemented new features and fixed bugs."
            ]
        },
        {
            "position": "Grado en Ingeniería Robótica - Universidad de Alicante",
            "dates": "Sep 2015 - Jul 2019",
            "description_points": [
                "Assisted in the development of internal tools.",
                "Participated in code reviews.",
                "Contributed to the company’s open-source projects."
            ]
        }
    ]

experiences = [
        {
            "position": "Data Engineering Senior Analyst - Accenture",
            "dates": "Ago 2022 - Actualidad",
            "description_points": [
                "Developed and maintained web applications.",
                "Collaborated with cross-functional teams.",
                "Implemented new features and fixed bugs."
            ]
        },
        {
            "position": "BI Developer - Mercanza",
            "dates": "Sep 2020 - Ago 2022",
            "description_points": [
                "Assisted in the development of internal tools.",
                "Participated in code reviews.",
                "Contributed to the company’s open-source projects."
            ]
        }
    ]

projects = [
        {
            "image_url": "https://via.placeholder.com/100",
            "title": "Project 1",
            "project_url": "https://www.example.com/project1",
            "description": "This is a brief description of Project 1."
        },
        {
            "image_url": "https://via.placeholder.com/100",
            "title": "Project 2",
            "project_url": "https://www.example.com/project2",
            "description": "This is a brief description of Project 2."
        }
    ]


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
            heading("Habilidades"),
            skills_grid(["Python","SQL","AWS","Machine Learning","Qlik Sense", "PowerBI"]),
            rx.divider(),
            heading("Proyectos"),
            project_grid(projects),
            rx.divider(),
            # heading("Experiencia"),
            # experience_grid(experiences),
            # rx.divider(),
            # heading("Formación"),
            # experience_grid(academic),
            # rx.divider(),
            heading("Extra"),
            rx.divider(),
            footer(),
            # end
            max_width=MAX_WIDTH,
            padding=EM_SIZE.SMALL,
            width="100%"
        )
    )


app = rx.App(    
    head_components=[
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={G_TAG}"),
        rx.script(
            f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{G_TAG}');
            """
        ),
        
    ],
    theme=rx.theme(
        appearance="light",
        accent_color="gray",
        radius="full"
    )
)

app.add_page(index)
