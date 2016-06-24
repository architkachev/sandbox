def merge(iterable, interval):
    result = []
    switcher = False
    for i in iterable:
        if interval[1] < i[0] or interval[0] > i[1]:
            if switcher:
                result.append(interval)
            result.append(i)
            switcher = False
        else:
            interval[0] = i[0] if interval[0] > i[0] else interval[0]
            interval[1] = interval[1] if i[1] < interval[1] else i[1]
            switcher = True
    return result


i = [[1, 5], [6, 15], [20, 21], [23, 26], [27, 30], [35, 40]]
j = [14, 33]

print merge(i, j)
