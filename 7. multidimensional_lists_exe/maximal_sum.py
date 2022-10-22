n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
max_matrix = []
for r in range(n-2):
    for c in range(m-2):
        current_sum = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2]\
        + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2] + \
                      matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]

        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix.clear()
            max_matrix.append([matrix[r][c], matrix[r][c+1], matrix[r][c+2]])
            max_matrix.append([matrix[r+1][c], matrix[r+1][c + 1], matrix[r+1][c + 2]])
            max_matrix.append([matrix[r+2][c], matrix[r+2][c + 1], matrix[r+2][c + 2]])

print(f"Sum = {max_sum}")
for row in max_matrix:
    print(' '.join(str(x) for x in row))
