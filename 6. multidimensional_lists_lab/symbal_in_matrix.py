n = int(input())

matrix = []

for _ in range(n):
    row = [x for word in input() for x in word]
    matrix.append(row)

symbol = input()

occurrence = []

for i in range(n):
    if symbol in matrix[i]:
        occurrence.append(i)
        occurrence.append(matrix[i].index(symbol))
        break

occurrence = tuple(occurrence)
if occurrence:
    print(occurrence)
else:
    print(f"{symbol} does not occur in the matrix")