from turtle import Screen, Turtle

from .utils import pixelart, next_pow_of_2


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

    pixelart(dolphin, Turtle(), 1, (-w / 2, h / 2))

    wn.mainloop()
