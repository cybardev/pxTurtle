from dataclasses import dataclass
from turtle import Turtle


@dataclass
class Pixel:
    x_pos: int
    y_pos: int
    color: str = "#ffffff"
    scale: int = 1

    def __post_init__(self):
        self.t = Turtle()
        self._SIZE: int = 10

    @property
    def pos(self) -> tuple[int, int]:
        return self.x_pos, self.y_pos

    @pos.setter
    def pos(self, new_pos: tuple[int, int]):
        self.x_pos, self.y_pos = new_pos

    def draw(self):
        self.t.penup()
        self.t.goto(
            self.x_pos * self.scale * self._SIZE, -self.y_pos * self.scale * self._SIZE
        )
        self.t.setheading(90)
        self.t.color(self.color)
        self.t.pendown()
        self.t.begin_fill()
        # draw scaled pixel
        for _ in range(4):
            self.t.fd(self.scale * self._SIZE)
            self.t.left(90)
        self.t.end_fill()


@dataclass
class Rect:
    x_pos: int
    y_pos: int
    width: int
    height: int
    color: str = "#000000"
    scale: int = 1

    def __post_init__(self):
        self._t = Turtle()
        self._px = Pixel(self.x_pos, self.y_pos, self.color, self.scale, self.t)

    @property
    def t(self) -> Turtle:
        return self._t

    @t.setter
    def t(self, new_t: Turtle):
        self._t = new_t
        self._px.t = new_t

    @property
    def pos(self) -> tuple[int, int]:
        return self.x_pos, self.y_pos

    @pos.setter
    def pos(self, new_pos: tuple[int, int]):
        self.x_pos, self.y_pos = new_pos

    @property
    def size(self) -> tuple[int, int]:
        return self.width, self.height

    @size.setter
    def size(self, new_size: tuple[int, int]):
        self.width, self.height = new_size

    def draw(self):
        for row in self.height:
            for col in self.width:
                self._px.pos = self.x_pos + col, -(self.y_pos + row)
                self._px.draw()
