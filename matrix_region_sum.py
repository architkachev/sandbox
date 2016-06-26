def precomputeSums(matrix):
    topRow, bottomRow = (0, len(matrix) - 1)
    leftCol, rightCol = (0, len(matrix[0]) - 1)
    sums = [[0] * (rightCol - leftCol + 1) for i in range(bottomRow - topRow + 1)]
    sums[topRow][leftCol] = matrix[topRow][leftCol]

    for col in range(leftCol + 1, rightCol + 1):
        sums[topRow][col] = sums[topRow][col - 1] + matrix[topRow][col]
    for row in range(topRow + 1, bottomRow + 1):
        sums[row][leftCol] = sums[row - 1][leftCol] + matrix[row][leftCol]

    for col in range(leftCol + 1, rightCol + 1):
        columnSum = matrix[topRow][col]
        for row in range(topRow + 1, bottomRow + 1):
            sums[row][col] = sums[row][col - 1] + matrix[row][col] + columnSum
            columnSum += matrix[row][col]

    return sums


def precompute(matrix):
    sum = [[0] * (len(matrix[0])) for _ in range(len(matrix))]
    sum[0][0] = matrix[0][0]

    for i in range(1, len(matrix[0])):
        sum[0][i] = sum[0][i - 1] + matrix[0][i]
    for i in range(1, len(matrix)):
        sum[i][0] = sum[i - 1][0] + matrix[i][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + matrix[i][j]

    return sum


def matrixRegionSum2(matrix, A, D, sums):
    if len(matrix) == 0:
        return

    if A[0] == 0 or A[1] == 0:
        OA = 0
    else:
        OA = sums[A[0] - 1][A[1] - 1]

    if A[1] == 0:
        OC = 0
    else:
        OC = sums[D[0]][A[1] - 1]

    if A[0] == 0:
        OB = 0
    else:
        OB = sums[A[0] - 1][D[1]]

    OD = sums[D[0]][D[1]]

    return OD - OB - OC + OA


matrix = [[1, 2, 3, 4, 5],
          [1, 2, 3, 4, 5],
          [1, 2, 3, 4, 5],
          [1, 2, 3, 4, 5],
          [1, 2, 3, 4, 5],
          [1, 2, 3, 4, 5]]

sums_my = [[1, 3, 6, 10, 15],
           [2, 4, 7, 11, 16],
           [3, 5, 8, 12, 17],
           [4, 6, 9, 13, 18],
           [5, 7, 10, 14, 19],
           [6, 8, 11, 15, 20]]

sums = precompute(matrix)
sums2 = precomputeSums(matrix)
#
# print(matrixRegionSum2(matrix, (1, 1), (2, 2), sums))

# print(sums)
# print(sums2)


result = [[0]*len(matrix[0])]*len(matrix)
print result

