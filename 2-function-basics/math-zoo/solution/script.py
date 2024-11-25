#!/usr/bin/env python3

from math import floor, ceil, atan, modf, nextafter, inf, cbrt

def zoo(number):
    return (
        floor(number),
        ceil(number),
        atan(number),
        modf(number),
        nextafter(number, -inf),
        cbrt(number)
    )

