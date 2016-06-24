def find_even(arr):
    return reduce(lambda a, x: a^x, arr + list(set(arr)))


arr = [1,2,2,2,2,3,4,5,5,5]

print find_even(arr)
