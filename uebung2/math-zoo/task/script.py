#!/usr/bin/env python3
import math

def zoo(number):

    # return a tuple containing the required values
    teil1 = (math.fmod(number, 1), math.trunc(number))
    teil2 = (math.floor(number), math.ceil(number), math.atan(number), teil1, math.nextafter(number, -math.inf), math.cbrt(number))
    return teil2