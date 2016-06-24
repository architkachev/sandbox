import heapq


def get_kth_largest(k, arr):
    # return heapq.nlargest(k, arr)
    maximum = [arr[0]] * k

    def min(arr):
        min_i = 0
        min = arr[0]
        for i in range(len(arr)):
            if min > arr[i]:
                min = arr[i]
                min_i = i
        return (min, min_i)

    for el in arr:
        min_plus_i = min(maximum)
        if min_plus_i[0] < el:
            maximum[min_plus_i[1]] = el

    return min(maximum)[0]


a = [1, 2, 3, 4, 65, 576, 5, 868, 69, 9, 790, 4567]

print get_kth_largest(5, a)


# def fibI():
#     a, b = 0, 1
#     while True:
#         a, b = b, a + b
#         yield a
#
#
# itera = fibI()
# for i in range(100000):
#     itera.next()
#
# print itera.next()
#
#
# def fibon(n):
#     return reduce(lambda a, x: (a[0] + a[1], a[0]), [(1, 1)] * (n-2))[0]
#
# print fibon(100002)
