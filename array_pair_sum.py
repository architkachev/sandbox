def get_pairs_sum(array, sum):
    array.sort()
    result = []
    s = 0
    e = len(array) - 1
    while s < e:
        if array[s] + array[e] == sum:
            result.append((array[s], array[e]))
            s += 1
        elif array[s] + array[e] < sum:
            s += 1
        else:
            e -= 1
    return result

if __name__ == "__main__":
    a = [2, 5, 7, 9, 4, 10, 13, 1]
    print(get_pairs_sum(a, 14))
