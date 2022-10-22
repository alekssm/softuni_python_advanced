def get_knight_hits(matrix, knight):
    hits = 0
    r, c = knight
    try:
        cell = matrix[r-1][c-2]
        if r-1 >= 0 and c-2 >= 0:
            if cell == "K":
                hits += 1

    except IndexError:
        pass

    try:
        cell = matrix[r-2][c-1]
        if r - 2 >= 0 and c - 1 >= 0:
            if cell == "K":
                hits += 1
    except IndexError:
        pass

    try:
        cell = matrix[r-2][c+1]
        if r - 2 >= 0 and c + 1 >= 0:
            if cell == "K":
                hits += 1
    except IndexError:
        pass

    try:
        cell = matrix[r-1][c+2]
        if r - 1 >= 0 and c + 2 >= 0:
            if cell == "K":
                hits += 1
    except IndexError:
        pass

    try:
        cell = matrix[r+1][c+2]
        if r + 1 >= 0 and c + 2 >= 0:
            if cell == "K":
                hits += 1
    except IndexError:
        pass

    try:
        cell = matrix[r+2][c+1]
        if r + 2 >= 0 and c + 1 >= 0:
            if cell == "K":
                hits += 1
    except IndexError:
        pass

    try:
        cell = matrix[r+2][c-1]
        if r + 2 >= 0 and c - 1 >= 0:
            if cell == "K":
                hits += 1
    except IndexError:
        pass

    try:
        cell = matrix[r+1][c-2]
        if r + 1 >= 0 and c - 2 >= 0:
            if cell == "K":
                hits += 1
    except IndexError:
        pass

    return hits


n = int(input())

matrix = []
knights_positions = []


for i in range(n): # matrix and positions of knights
    row = []
    current_line = input()
    for j in range(n):
        current_cell = current_line[j]
        if current_cell == "K":
            knights_positions.append((i, j))
        row.append(current_cell)
    matrix.append(row)

removed_knights = 0

while True:
    max_hits = 0
    max_knight = ()

    for knight in knights_positions:
        hits = get_knight_hits(matrix, knight)
        if hits > max_hits:
            max_hits = hits
            max_knight = knight

    if max_hits == 0:
        break

    matrix[max_knight[0]][max_knight[1]] = "0"
    knights_positions.remove(max_knight)
    removed_knights += 1

print(removed_knights)

