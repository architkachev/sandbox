def squareroot(n):
    if n < 0:
        raise ValueError
    if n == 1:
        return 1
    result = 1
    for i in range(n / 2 + 1):
        if i ** 2 == n:
            return i
        elif i ** 2 > n:
            return i - 1
    return result


def squareroot2(n):
    pass


print(squareroot(1))
