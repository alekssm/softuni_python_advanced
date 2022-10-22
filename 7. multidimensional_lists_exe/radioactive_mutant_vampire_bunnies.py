from collections import deque

n, m = [int(x) for x in input().split()]

matrix = []

player = []
bunnies = []
for r in range(n):
    row = []
    o = input()
    for c in range(m):
        el = o[c]
        if el == "P":
            player.append(r)
            player.append(c)
        elif el == "B":
            bunny = (r, c)
            bunnies.append(bunny)
        row.append(el)
    matrix.append(row)

commands = deque(ch for ch in input())

win = False
lose = False

while True:
    command = commands.popleft()
    if command == "U":
        if player[0] - 1 < 0:
            win = True
            matrix[player[0]][player[1]] = "."
        else:
            if matrix[player[0] - 1][player[1]] == "B":
                matrix[player[0]][player[1]] = "."
                player[0] -= 1
                lose = True
            else:
                matrix[player[0] - 1][player[1]] = "P"
                matrix[player[0]][player[1]] = "."
                player[0] -= 1
    if command == "D":
        if player[0] + 1 == n:
            win = True
            matrix[player[0]][player[1]] = "."
        else:
            if matrix[player[0] + 1][player[1]] == "B":
                matrix[player[0]][player[1]] = "."
                player[0] += 1
                lose = True
            else:
                matrix[player[0] + 1][player[1]] = "P"
                matrix[player[0]][player[1]] = "."
                player[0] += 1
    if command == "R":
        if player[1] + 1 == m:
            win = True
            matrix[player[0]][player[1]] = "."
        else:
            if matrix[player[0]][player[1] + 1] == "B":
                matrix[player[0]][player[1]] = "."
                player[1] += 1
                lose = True
            else:
                matrix[player[0]][player[1] + 1] = "P"
                matrix[player[0]][player[1]] = "."
                player[1] += 1
    if command == "L":
        if player[1] - 1 < 0:
            win = True
            matrix[player[0]][player[1]] = "."
        else:
            if matrix[player[0]][player[1] - 1] == "B":
                matrix[player[0]][player[1]] = "."
                player[1] -= 1
                lose = True
            else:
                matrix[player[0]][player[1] - 1] = "P"
                matrix[player[0]][player[1]] = "."
                player[1] -= 1
    new_bunnies = []    # set will be optimal
    for b in bunnies:
        if b[0] - 1 >= 0:
            if matrix[b[0] - 1][b[1]] == "P":
                lose = True
            matrix[b[0] - 1][b[1]] = "B"
            new_bunnies.append((b[0] - 1, b[1]))
        if b[0] + 1 < n:
            if matrix[b[0] + 1][b[1]] == "P":
                lose = True
            matrix[b[0] + 1][b[1]] = "B"
            new_bunnies.append((b[0] + 1, b[1]))
        if b[1] + 1 < m:
            if matrix[b[0]][b[1] + 1] == "P":
                lose = True
            matrix[b[0]][b[1] + 1] = "B"
            new_bunnies.append((b[0], b[1] + 1))
        if b[1] - 1 >= 0:
            if matrix[b[0]][b[1] - 1] == "P":
                lose = True
            matrix[b[0]][b[1] - 1] = "B"
            new_bunnies.append((b[0], b[1] - 1))
    if win or lose:
        break
    bunnies += new_bunnies

for ll in matrix:
    print("".join(ll))
if win:
    print(f"won: {player[0]} {player[1]}")
else:
    print(f"dead: {player[0]} {player[1]}")
