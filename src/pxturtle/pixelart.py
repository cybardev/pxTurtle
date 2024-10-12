import tkinter as tk
import turtle

from dataclasses import dataclass

from .utils import Pixel, Rect


@dataclass
class PixelArt:
    pixels: list[Pixel | Rect]
    bg_color: str = "#ffffff"
    scale: int = 1

    def __post_init__(self):
        self.t = turtle.Turtle()

    def draw(self):
        self.t.speed(0)
        self.t.hideturtle()
        for px in self.pixels:
            px.t = self.t
            px.scale = self.scale
            px.draw()


@dataclass
class Canvas:
    art: PixelArt
    width: int
    height: int
    bg_color: str = "#ffffff"

    def __post_init__(self):
        self._root = tk.Tk()

        self._canvas = turtle.ScrolledCanvas(
            self._root, self.width, self.height, self.width, self.height
        )
        self._canvas.pack(side=tk.LEFT)

        self._screen = turtle.TurtleScreen(self._canvas)
        self._screen.setworldcoordinates(-10, 100, 100, -10)

        self._t = turtle.RawTurtle(self._screen)

    def draw(self):
        self._t.goto(0, 0)

        self.art.t = self._t
        self.art.draw()

        self._screen.mainloop()

    def save(self, filename: str, path: str = "."):
        self._canvas.postscript(file=f"{path}/{filename}.eps")
