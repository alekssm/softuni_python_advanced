n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append([x for x in input().split()])

square_matrices = 0

for r in range(n - 1):
    for c in range(m - 1):
        if matrix[r][c] == matrix[r+1][c] == matrix[r][c+1] == matrix[r+1][c+1]:
            square_matrices += 1

print(square_matrices)
