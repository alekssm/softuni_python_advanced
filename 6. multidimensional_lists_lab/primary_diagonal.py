n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

result = 0

for i in range(n):
    result += matrix[i][i]

print(result)