from dataclasses import dataclass
from turtle import Turtle


@dataclass
class Pixel:
    x_pos: int
    y_pos: int
    color: str = "#ffffff"
    scale: int = 1

    @property
    def pos(self) -> tuple[int, int]:
        return self.x_pos, self.y_pos

    @pos.setter
    def pos(self, pos: tuple[int, int]):
        self.x_pos, self.y_pos = pos


@dataclass
class Pen:
    t: Turtle
    color: str = "#000000"
    pixel_scale: int = 1

    def __post_init__(self):
        init_pos = (0, 0)
        self._pixel = Pixel(*init_pos, self.color, self.pixel_scale)

    def draw(self, x, y):
        PIXEL_SIZE: int = 10
        self.t.penup()
        self.t.goto(
            x * self.pixel_scale * PIXEL_SIZE, -y * self.pixel_scale * PIXEL_SIZE
        )
        self.t.setheading(90)
        self.t.color(self.color)
        self.t.pendown()
        self.t.begin_fill()
        # draw scaled pixel
        for _ in range(4):
            self.t.fd(self.pixel_scale * PIXEL_SIZE)
            self.t.left(90)
        self.t.end_fill()


@dataclass
class Rect:
    x_pos: int
    y_pos: int
    width: int
    height: int
    t: Turtle
    color: str = "#000000"
    pixel_scale: int = 1

    def __post_init__(self):
        self._pen = Pen(self.t, self.color, self.pixel_scale)

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
        pass


def pixel(
    pen: Turtle,
    color: str,
    row: int,
    col: int,
    scale: int,
    x_offset: int,
    y_offset: int,
):
    PIXEL_SIZE: int = 10
    pen.penup()
    pen.goto(col * scale * PIXEL_SIZE + x_offset, -row * scale * PIXEL_SIZE + y_offset)
    pen.setheading(90)
    pen.color(color)
    pen.pendown()
    pen.begin_fill()
    # draw scaled pixel
    for _ in range(4):
        pen.fd(scale * PIXEL_SIZE)
        pen.left(90)
    pen.end_fill()


def pixelart(
    px_grid: list,
    pen: Turtle,
    scale: int = 1,
    pos_offset: tuple[int, int] = (0, 0),
):
    """
    Draw pixel art according to ls
    """
    pen.speed(0)
    pen.hideturtle()
    for row_idx, row in enumerate(px_grid):
        for col_idx, px_color in enumerate(row):
            if px_color:
                pixel(
                    pen,
                    px_color,
                    row_idx,
                    col_idx,
                    scale,
                    pos_offset[0],
                    pos_offset[1],
                )


def next_pow_of_2(x: int):
    return 1 << (x - 1).bit_length()
