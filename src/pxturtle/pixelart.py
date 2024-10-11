from dataclasses import dataclass
from turtle import Turtle

from .utils import Pixel, Rect


@dataclass
class PixelArt:
    pixels: list[Pixel | Rect]
    bg_color: str = "#ffffff"
    scale: int = 1

    def __post_init__(self):
        self.t = Turtle()

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

    def draw(self, **kwargs):
        pass

    def save(self, format: str = "png"):
        pass
