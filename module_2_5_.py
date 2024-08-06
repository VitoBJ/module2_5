def get_matrix(n, m, value):
    matrix = []

    for _ in range(n):
        row = []

        for _ in range(m):
            row.append(value)

        matrix.append(row)

    return matrix



n = 9
m = 5
value = 45
result_matrix = get_matrix(n, m, value)


for row in result_matrix:
    print(row)
