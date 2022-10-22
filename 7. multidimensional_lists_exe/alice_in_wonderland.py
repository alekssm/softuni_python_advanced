n = int(input())

matrix = []
alice_position = ()

# matrix and the position of Alice
for i in range(n):
    current_row = input().split()
    for j in range(n):
        cell = current_row[j]
        if cell == "A":
            alice_position = (i, j)
    matrix.append(current_row)

collected_tea = 0

command = input()
while command:
    if command == "up":
        new_r = alice_position[0] - 1
        new_c = alice_position[1]
        matrix[alice_position[0]][alice_position[1]] = "*"
        if new_r < 0:
            break

        new_position = matrix[new_r][new_c]
        if new_position == "R":
            matrix[new_r][new_c] = "*"
            break

        if new_position.isdigit():
            collected_tea += int(new_position)
        matrix[new_r][new_c] = "*"
        alice_position = (new_r, new_c)

    elif command == "down":
        new_r = alice_position[0] + 1
        new_c = alice_position[1]
        matrix[alice_position[0]][alice_position[1]] = "*"
        if new_r >= len(matrix):
            break

        new_position = matrix[new_r][new_c]
        if new_position == "R":
            matrix[new_r][new_c] = "*"
            break

        if new_position.isdigit():
            collected_tea += int(new_position)
        matrix[new_r][new_c] = "*"
        alice_position = (new_r, new_c)

    elif command == "right":
        new_r = alice_position[0]
        new_c = alice_position[1] + 1
        matrix[alice_position[0]][alice_position[1]] = "*"
        if new_c >= len(matrix):
            break

        new_position = matrix[new_r][new_c]
        if new_position == "R":
            matrix[new_r][new_c] = "*"
            break

        if new_position.isdigit():
            collected_tea += int(new_position)
        matrix[new_r][new_c] = "*"
        alice_position = (new_r, new_c)

    if command == "left":
        new_r = alice_position[0]
        new_c = alice_position[1] - 1
        matrix[alice_position[0]][alice_position[1]] = "*"
        if new_c < 0:
            break

        new_position = matrix[new_r][new_c]
        if new_position == "R":
            matrix[new_r][new_c] = "*"
            break

        if new_position.isdigit():
            collected_tea += int(new_position)
        matrix[new_r][new_c] = "*"
        alice_position = (new_r, new_c)

    if collected_tea >= 10:
        break

    command = input()

if collected_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(' '.join(row))
