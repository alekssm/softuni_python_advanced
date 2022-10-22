n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])


bombs = input().split() # a list of all bombs

while bombs:
    rb, cb = map(int, bombs.pop(0).split(",")) # coordinates of the current bomb

    if abs(rb) >= n or abs(cb) >= n:
        continue

    bomb_power = matrix[rb][cb]
    if bomb_power <= 0:
        continue

    for b in range(rb-1, rb+2):
        for j in range(cb-1, cb+2):
            try:
                if matrix[b][j] > 0 and b >= 0 and j >= 0:
                    matrix[b][j] -= bomb_power
            except IndexError:
                pass

alive_cells = []
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells.append(el)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    print(' '.join(str(x) for x in row))


