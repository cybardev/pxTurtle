from turtle import Screen, Turtle


def px_draw(
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


def px_grid_draw(
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
                px_draw(
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


if __name__ == "__main__":
    a = "black"
    b = "white"
    c = "lightcyan"
    d = "turquoise"

    dolphin = [
        ["", "", "", "", "", "", "", "", a, a, "", "", "", "", ""],
        ["", "", "", "", "", "", "", a, d, a, "", "", "", "", ""],
        ["", "", "", "", a, a, a, d, d, a, a, "", "", "", ""],
        ["", "", "", a, d, d, d, d, c, c, d, a, "", "", ""],
        ["", "", a, d, b, b, c, c, c, c, c, d, a, "", ""],
        ["", a, a, d, a, b, c, c, c, c, c, c, d, a, ""],
        [a, d, d, c, c, c, c, d, b, b, c, c, c, a, ""],
        ["", a, a, a, a, a, a, d, d, a, b, c, c, d, a],
        ["", "", "", "", a, c, a, a, d, a, a, b, c, c, a],
        ["", "", "", "", "", a, "", "", a, a, "", a, c, c, a],
        ["", "", "", "", "", "", "", "", "", "", "", a, c, a, ""],
        ["", "", "", "", "", "", "", "", "", "", a, a, c, a, ""],
        ["", "", "", "", "", "", "", "", "", a, c, c, a, "", ""],
        ["", "", "", "", "", "", "", "", "", "", a, c, a, "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", a, "", "", ""],
    ]

    h = 10 * next_pow_of_2(len(dolphin))
    w = 10 * next_pow_of_2(len(dolphin[0]))
    print(w, h)

    wn = Screen()
    wn.setup(w, h)
    wn.tracer(0)

    px_grid_draw(dolphin, Turtle(), 1, (-w / 2, h / 2))

    wn.mainloop()
