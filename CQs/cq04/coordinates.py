__author__ = "730813516"


def get_coords(xs: str, ys: str) -> None:
    # print the formatted pairs of each character in the two input strings.
    countX = 0
    countY = 0
    while countX != len(xs):
        while countY != len(ys):
            print("(" + xs[countX] + "," + ys[countY] + ")")
            countY += 1
        countY = 0
        countX += 1
