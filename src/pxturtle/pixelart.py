from dataclasses import dataclass
from turtle import Turtle

from .utils import Pixel, Rect


@dataclass
class PixelArt:
    t: Turtle
    bg_color: str = "#ffffff"
    px_scale: int = 1

    def draw(self, pixels: list[Pixel | Rect]):
        self.t.speed(0)
        self.t.hideturtle()
        for px in pixels:
            px.t = self.t
            px.scale = self.px_scale
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
