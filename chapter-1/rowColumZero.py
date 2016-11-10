

def makeZero(matrix):
    row = len(matrix)
    col = len(matrix[0])
    list = []
    for i in range(0, row):
        for j in range(0, col):
            if matrix[i][j] == 0:
                list.append((i,j))

    if list:
        for elem in list:
            row1, col1 = elem
            for i in range(0, col):
                matrix[row1][i] = 0
            for i in range(0, row):
                matrix[i][col1] = 0

    return matrix



if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 0, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 0, 16]
    ]
    for m in matrix:
        print m
    print "After making Zeroes..."
    matrix = makeZero(matrix)

    for m in matrix:
        print m