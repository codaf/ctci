


def rotateMatrixRight(matrix):
    N = len(matrix[0])

    for i in range(0, N/2):
        for j in range(i, N-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N-j-1][i]
            matrix[N-j-1][i] = matrix[N-i-1][N-j-1]
            matrix[N-i-1][N-j-1] = matrix[j][N-i-1]
            matrix[j][N-i-1] = temp
    return matrix

def rotateMatrixLeft(matrix):
    N = len(matrix[0])

    for i in range(0, N/2):
        for j in range(i, N-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][N-i-1]
            matrix[j][N-i-1] = matrix[N-i-1][N-j-1]
            matrix[N-i-1][N-j-1] = matrix[N-j-1][i]
            matrix[N-j-1][i] = temp
    return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    for m in matrix:
        print m

    matrixRight = rotateMatrixRight(matrix)
    print "After Rotating 90 Degree right"
    for m in matrixRight:
        print m
    # Need to Initialize Again here ..??? WHY
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    matrixLeft = rotateMatrixLeft(matrix)
    print "After Rotating 90 Degree left"
    for m in matrixLeft:
        print m