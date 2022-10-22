def read_matrix():
    n, m = [int(x) for x in input().split(", ")]
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()

sum_of_all = 0

for r in matrix:
    sum_of_all += sum(r)

print(sum_of_all)
print(matrix)