import copy

d1 = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

d2 = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def get_dict_count(d):
    result = copy.deepcopy(d)
    for key in result:
        result[key] = len(result[key])
    return result


d11 = get_dict_count(d1)
d22 = get_dict_count(d2)


def get_first_part_count(n):
    result = []
    h = n / 100
    if h > 0:
        result.append(d11[h])
        result.append(len("hundred"))
    return result


def get_first_part(n):
    result = []
    h = n / 100
    if h > 0:
        result.append(d1[h])
        result.append("hundred")
    return result


def get_second_part(n):
    # first_part.append("and")
    result = []
    h = n % 100
    if h in d1.keys():
        result.append(d1[h])
    elif h in d2.keys():
        result.append(d2[h])
    elif h != 0:
        first = h / 10
        second = h % 10
        result.append("{0}-{1}".format(d2[first * 10], d1[second]))
    return result


def get_second_part_count(n):
    # first_part.append("and")
    result = []
    h = n % 100
    if h in d1.keys():
        result.append(d11[h])
    elif h in d2.keys():
        result.append(d22[h])
    elif h != 0:
        first = h / 10
        second = h % 10
        result.append(d22[first * 10])
        result.append(d11[second])
    return result


def get_str_repr(n):
    res = []
    fp = get_first_part(n)
    sp = get_second_part(n)
    res.extend(fp)
    if len(fp) != 0 and len(sp) != 0:
        res.extend(["and"])
    res.extend(sp)
    return res


def get_total_count(n):
    return reduce(lambda a, x: a + x, get_first_part_count(n)) \
           + reduce(lambda a, x: a + x, get_second_part_count(n))


n = 165
print(get_str_repr(n))
print(get_total_count(n))
