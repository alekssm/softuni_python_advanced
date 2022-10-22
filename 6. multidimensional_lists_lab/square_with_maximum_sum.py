n, m = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

max = 0
max_row = 0
max_col = 0
for i in range(n-1):
    for j in range(m-1):
        curr_sum = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
        if curr_sum > max:
            max, max_row, max_col = curr_sum, i, j

print(matrix[max_row][max_col], matrix[max_row][max_col+1])
print(matrix[max_row+1][max_col], matrix[max_row+1][max_col+1])
print(max)