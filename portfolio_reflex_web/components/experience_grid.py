import reflex as rx

# Definición de un componente para una experiencia laboral
def experience_card(position, dates, description_points):
    return rx.box(
        rx.heading(position, size="2"),
        rx.text(dates, font_style="italic"),
        rx.unordered_list(
            *[rx.list_item(point) for point in description_points]
        ),
        shadow="md",
        border_radius="lg",
        padding="4",
        max_width="md",
        margin="4",
        bg="white",
        # border="1px solid lightgray"
    )

# Definición de un componente Grid de Experiencias Laborales
def experience_grid(experiences):
    return rx.grid(
        *[experience_card(exp["position"], exp["dates"], exp["description_points"]) for exp in experiences],
        template_columns="repeat(auto-fill, minmax(300px, 1fr))",
        gap="1rem",
        padding="4",
    )
