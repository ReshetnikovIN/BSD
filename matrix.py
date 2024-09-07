def get_matrix(n, m, value):
    n = int(n)
    m = int(m)
    matrix = []
    matrixx = []
    i = 0
    j = 0
    for i in range(0, n, 1):
        for j in range(0, m, 1):
            matrixx.append(value)
        matrix.append(matrixx)
        matrixx = []
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)