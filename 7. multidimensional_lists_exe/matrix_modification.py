n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()
    if command[0] == "END":
        break

    if len(command) != 4:
        continue

    action = command[0]
    row, col, value = (int(x) for x in command[1:])

    if row < 0 or row >= n or col < 0 or col >= n:
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

for r in matrix:
    print(' '.join(str(x) for x in r))
