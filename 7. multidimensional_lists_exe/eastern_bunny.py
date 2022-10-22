def get_up_eggs(matrix, bunny):
    eggs = 0
    cells = []
    br, cb = bunny  # starting row, column of the bunny
    if br == 0:
        pass
    else:
        for i in range(br - 1, -1, -1):
            cell = matrix[i][cb]
            if cell == "X":
                break
            eggs += int(matrix[i][cb])
            cells.append([i, cb])
    return eggs, cells, "up"


def get_down_eggs(matrix, bunny):
    eggs = 0
    cells = []
    br, cb = bunny  # starting row, column of the bunny
    if br == len(matrix) - 1:
        pass
    else:
        for i in range(br + 1, len(matrix)):
            cell = matrix[i][cb]
            if cell == "X":
                break
            eggs += int(matrix[i][cb])
            cells.append([i, cb])
    return eggs, cells, "down"


def get_right_eggs(matrix, bunny):
    eggs = 0
    cells = []
    br, cb = bunny  # starting row, column of the bunny
    if cb == len(matrix) - 1:
        pass
    else:
        for i in range(cb + 1, len(matrix)):
            cell = matrix[br][i]
            if cell == "X":
                break
            eggs += int(matrix[br][i])
            cells.append([br, i])
    return eggs, cells, "right"


def get_left_eggs(matrix, bunny):
    eggs = 0
    cells = []
    br, cb = bunny  # starting row, column of the bunny
    if cb == 0:
        pass
    else:
        for i in range(cb - 1, -1, -1):
            cell = matrix[br][i]
            if cell == "X":
                break
            eggs += int(matrix[br][i])
            cells.append([br, i])
    return eggs, cells, "left"

n = int(input())

matrix = []
bunny_position = ()

# matrix and the position of the bunny
for i in range(n):
    current_row = input().split()
    for j in range(n):
        cell = current_row[j]
        if cell == "B":
            bunny_position = (i, j)
    matrix.append(current_row)


up_eggs = get_up_eggs(matrix, bunny_position)
down_eggs = get_down_eggs(matrix, bunny_position)
right_eggs = get_right_eggs(matrix, bunny_position)
left_eggs = get_left_eggs(matrix, bunny_position)

max_eggs = 0
best_path = ()

if up_eggs[0] > max_eggs:
    max_eggs = up_eggs[0]
    best_path = up_eggs
if down_eggs[0] > max_eggs:
    max_eggs = down_eggs[0]
    best_path = down_eggs
if right_eggs[0] > max_eggs:
    max_eggs = right_eggs[0]
    best_path = right_eggs
if left_eggs[0] > max_eggs:
    max_eggs = left_eggs[0]
    best_path = left_eggs

print(best_path[2])
for item in best_path[1]:
    print(item)
print(best_path[0])
