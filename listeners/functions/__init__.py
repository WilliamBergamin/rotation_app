from slack_bolt import App

from .setup import setup_function
from .rotate import rotate_function
from .read import read_function


def register(app: App):
    app.function("setup_function")(setup_function)
    app.function("rotate_function")(rotate_function)
    app.function("read_function")(read_function)
