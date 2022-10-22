n = 5

matrix = []
player_position = ()
targets = []
shot_targets = []

# matrix, player position, and targets positions
for i in range(n):
    current_row = input().split()
    for j in range(n):
        cell = current_row[j]
        if cell == "A":
            player_position = (i, j)
        elif cell == "x":
            targets.append((i, j))
    matrix.append(current_row)

num = int(input())

for _ in range(num):
    command = input().split()
    row = player_position[0]
    col = player_position[1]

    if command[0] == "move":
        distance = int(command[2])

        if command[1] == "up":
            if row - distance < 0:
                continue
            for i in range(row - 1, -1, -1):
                if matrix[i][col] == "x":
                    row = i + 1
                    continue
                row = i

        elif command[1] == "down":
            if row + distance >= n:
                continue
            for i in range(row + 1, n):
                if matrix[i][col] == "x":
                    row = i - 1
                    continue
                row = i

        elif command[1] == "right":
            if col + distance >= n:
                continue
            for i in range(col + 1, n):
                if matrix[row][i] == "x":
                    col = i - 1
                    continue
                col = i

        elif command[1] == "left":
            if col - distance < 0:
                continue
            for i in range(col - 1, -1, -1):
                if matrix[row][i] == "x":
                    col = i + 1
                    continue
                col = i

    elif command[0] == "shoot":
        if command[1] == "up":
            if row == 0:
                continue
            for i in range(row - 1, -1, -1):
                if matrix[i][col] == "x":
                    shot_targets.append([i, col])
                    matrix[i][col] = "."
                    break
        elif command[1] == "down":
            if row == n - 1:
                continue
            for i in range(row + 1, n):
                if matrix[i][col] == "x":
                    shot_targets.append([i, col])
                    matrix[i][col] = "."
                    break
        elif command[1] == "right":
            if col == n - 1:
                continue
            for i in range(col + 1, n):
                if matrix[row][i] == "x":
                    shot_targets.append([row, i])
                    matrix[row][i] = "."
                    break
        elif command[1] == "left":
            if col == 0:
                continue
            for i in range(col - 1, -1, -1):
                if matrix[row][i] == "x":
                    shot_targets.append([row, i])
                    matrix[row][i] = "."
                    break

        if len(shot_targets) == len(targets):
            break


if len(shot_targets) == len(targets):
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {len(targets) - len(shot_targets)} targets left.")

for target in shot_targets:
    print(target)
