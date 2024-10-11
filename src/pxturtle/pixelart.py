from dataclasses import dataclass

from .utils import Pixel, Rect


@dataclass(frozen=True)
class PixelArt:
    px_scale: int = 1

    def draw_rect(self):
        r = Rect()

    def paint_grid(self, px_grid: list[list[Pixel]]):
        pass


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
