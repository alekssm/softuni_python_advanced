n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append([x for x in input().split()])

while True:
    command = input().split()
    if command[0] == "END":
        break

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    if any(x for x in command[1:] if int(x) < 0):
        print("Invalid input!")
        continue

    r1, c1, r2, c2 = map(int, command[1:])

    if r1 >= n or r2 >= n or c1 >= m or c2 >= m:
        print("Invalid input!")
        continue

    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

    for row in matrix:
        print(' '.join(str(x) for x in row))

