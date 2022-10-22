n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(row)

print(matrix)