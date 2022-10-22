n, m = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

result = [0] * m

for r in matrix:
    for i in range(m):
        result[i] += r[i]

print(result)

result_from_values = [0] * m

for r in range(n):
    for j in range(m):
        value = matrix[r][j]
        result_from_values[j] += value

print(result_from_values)