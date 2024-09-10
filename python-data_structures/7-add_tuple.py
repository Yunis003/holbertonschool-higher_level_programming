#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    x1, x2 = tuple_a[:2]
    y1, y2 = tuple_b[:2]

    return (x1 + y1, x2+ y2)
