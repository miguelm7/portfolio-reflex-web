import reflex as rx

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"

class Size:
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px

SIZE = Size()

class EmSize():
    SMALL = "0.8em" 
    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"
    BIG = "4em"

EM_SIZE = EmSize()


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Ubuntu+Sans:ital,wght@0,100..800;1,100..800&display=swap"
]

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"
    },
    "font_family" : "Ubuntu Sans"
}