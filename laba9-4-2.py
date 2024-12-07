N = 4
A = [[1, -2, 3, -4],
     [-5, 6, -7, 8],
     [9, -10, 11, -12],
     [-13, 14, -15, 16]]

def digi2sign(matrix):
    err = 0
    prv = len(matrix[0])
    for row in A:
        err += len(row) != prv
        prv = len(row)
    err += len(matrix) != prv
    if not err:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] >= 0:
                    matrix[i][j] = 1
                elif matrix[i][j] < 0:
                    matrix[i][j] = 0
    else:
        print("Non-square.")
        raise ValueError

digi2sign(A)
for row in A:
    print(row)