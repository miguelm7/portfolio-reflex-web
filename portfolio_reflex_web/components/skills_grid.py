import reflex as rx
from typing import List

def card(content):
    return rx.card(
        rx.text(content, size="md"),
        shadow="md",
        border_radius="lg",
        padding="4",
        max_width="sm",
        margin="4",
        bg="white",
    )

def item_card(item: str)-> rx.Component:
    return rx.card(item)

def skills_grid(items)-> rx.Component:
    return rx.grid(
        *[card(item) for item in items],
        gap="1rem",
        grid_template_columns=[
            "1fr",
            "repeat(2, 1fr)",
            "repeat(2, 1fr)",
            "repeat(3, 1fr)",
            "repeat(4, 1fr)",
        ],
        width="100%",
    )