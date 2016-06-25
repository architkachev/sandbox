def findMissingNumber2(array1, array2):
    d = {}
    for num in array1:
        d[num] = 1
    for num in array2:
        if num not in d.keys():
            return num


def findMissingNumber3(array1, array2):
    result = 0
    for num in array1 + array2:
        result ^= num
    return result


print(findMissingNumber3([1, 2, 4], [1, 2, 3, 4]))
