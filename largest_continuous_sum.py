def largestContinuousSum(arr):
    if len(arr) == 0:
        return
    maxSum = currentSum = arr[0]
    for num in arr[1:]:
        currentSum = max(currentSum + num, num)
        maxSum = max(currentSum, maxSum)
    return maxSum


def sumArray(arr):
    res = []
    res.append(arr[0])
    for i in range(1, len(arr)):
        res.append(arr[i] + res[i - 1])
    return res


arr = [1, -6, 7, -5, 2, 1, 3]

print(largestContinuousSum(arr))
print(max(sumArray(arr)))
