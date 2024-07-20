import reflex as rx

# Definición de un componente para una tarjeta de proyecto
def project_card(image_url, title, project_url, description):
    return rx.card(
        rx.hstack(
            rx.image(src=image_url, box_size="100px", border_radius="lg"),
            rx.vstack(
                rx.link(
                    rx.heading(title, size="lg"),
                    href=project_url,
                    is_external=True,
                ),
                rx.text(description),
                align="start"
            ),
            align="center",
            spacing="4"
        ),
        shadow="md",
        border_radius="lg",
        padding="4",
        max_width="md",
        margin="4",
        bg="white",
        border="1px solid lightgray",
        width="100%",
    )

# Definición de un componente Grid de Proyectos
def project_grid(projects):
    return rx.grid(
        *[project_card(proj["image_url"], proj["title"], proj["project_url"], proj["description"]) for proj in projects],
        template_columns="repeat(auto-fill, minmax(300px, 1fr))",
        gap="1rem",
        padding="4",
        width="100%",
    )
