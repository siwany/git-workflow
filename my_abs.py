import math
import numbers

def my_abs(x):
    if isinstance(x, numbers.Real):
        if x < 0:
            return -x
        else:
            return x
    elif isinstance(x, numbers.Complex):
        return math.sqrt(
            x.real ** 2 + x.imag ** 2)
    else:
        return math.nanimport math

def my_abs(x):
    try:
        if x < 0:
            return -x
        else:
            return x
    except TypeError:
        return math.nan

def my_almost_eq(x, y):
    return my_abs(x - y) < 1e-16
