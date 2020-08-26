def matrix_mult(a, b):
    if len(a[0]) != len(b):
        return "invalid input"

    result = [[0 for _ in range(len(a))] for _ in range(len(b[0]))]
    
    for i in range(0, len(a)):
        for j in range(0, len(b[0])):
            for k in range(0, len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

a = [[1, 1],
    [2, 2]] 

b = [[1, 1],
    [2, 2]] 

print(matrix_mult(a, b))

