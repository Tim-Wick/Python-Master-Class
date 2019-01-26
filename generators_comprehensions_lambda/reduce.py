import functools


def calc_values(x, y: int):
    return x + y


numbers = [2, 3, 5, 8, 13]

reduce_value = functools.reduce(calc_values, numbers)
print(reduce_value)
