import math

def my_abs(x):
    try:
        if x < 0:
            return -x
        else:
            return x
    except TypeError:
        return math.nandef my_abs(x):
    if x < 0:
        return -x
    else:
        return x
