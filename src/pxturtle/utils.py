from turtle import Turtle


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
