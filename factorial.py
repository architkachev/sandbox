"""
>>> [factorial_reduce(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]
"""


def factorial_reduce(n):
    """
    >>> [factorial_reduce(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    """
    return reduce(lambda a, x: a * x, range(1, n + 1))


def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def fac(n, res=1):
    if n == 1:
        return res
    else:
        res *= n
        return fac(n - 1, res)
