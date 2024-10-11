from dataclasses import dataclass
from turtle import Turtle


@dataclass
class Pixel:
    x_pos: int
    y_pos: int
    color: str = "#ffffff"
    scale: int = 1
    t: Turtle = None

    def __post_init__(self):
        self._SIZE: int = 10
        if self.t is None:
            self.t = Turtle()

    @property
    def pos(self) -> tuple[int, int]:
        return self.x_pos, self.y_pos

    @pos.setter
    def pos(self, pos: tuple[int, int]):
        self.x_pos, self.y_pos = pos

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
        self._px = Pixel(self.x_pos, self.y_pos, self.color, self.scale, self._t)

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
    def pos(self, pos: tuple[int, int]):
        self.x_pos, self.y_pos = pos

    @property
    def size(self) -> tuple[int, int]:
        return self.width, self.height

    @size.setter
    def size(self, size: tuple[int, int]):
        self.width, self.height = size

    def draw(self):
        for row in self.height:
            for col in self.width:
                self._px.pos = self.x_pos + col, -(self.y_pos + row)
                self._px.draw()


def pixel(
    t: Turtle,
    color: str,
    row: int,
    col: int,
    scale: int,
    x_offset: int,
    y_offset: int,
):
    PIXEL_SIZE: int = 10
    t.penup()
    t.goto(col * scale * PIXEL_SIZE + x_offset, -row * scale * PIXEL_SIZE + y_offset)
    t.setheading(90)
    t.color(color)
    t.pendown()
    t.begin_fill()
    # draw scaled pixel
    for _ in range(4):
        t.fd(scale * PIXEL_SIZE)
        t.left(90)
    t.end_fill()


def pixelart(
    px_grid: list,
    t: Turtle,
    scale: int = 1,
    pos_offset: tuple[int, int] = (0, 0),
):
    """
    Draw pixel art according to ls
    """
    t.speed(0)
    t.hideturtle()
    for row_idx, row in enumerate(px_grid):
        for col_idx, px_color in enumerate(row):
            if px_color:
                pixel(
                    t,
                    px_color,
                    row_idx,
                    col_idx,
                    scale,
                    pos_offset[0],
                    pos_offset[1],
                )


def next_pow_of_2(x: int):
    return 1 << (x - 1).bit_length()
