n = int(input())
moves = input().split()

matrix = []

coal_on_field = 0
pl_r = 0      # row where the player is
pl_c = 0      # column where the player is /// position_of_the_player = matrix[pl_r][pl_c]
lost = False

for r in range(n):
    row = []
    for item in input().split():
        if item == "c":
            coal_on_field += 1
        elif item == "s":
            pl_r = r
            pl_c = len(row)
        row.append(item)
    matrix.append(row)

for move in moves:
    moving_to = [[]]        # new_player_position = matrix[new_r][new_c]
    new_r = 0               # the new row player will take
    new_c = 0               # the new column player will take

    if move == "up":
        try:
            moving_to = matrix[pl_r-1][pl_c]
        except IndexError:
            continue
        new_r = pl_r - 1
        new_c = pl_c

    elif move == "down":
        try:
            moving_to = matrix[pl_r+1][pl_c]
        except IndexError:
            continue
        new_r = pl_r + 1
        new_c = pl_c

    elif move == "right":
        try:
            moving_to = matrix[pl_r][pl_c+1]
        except IndexError:
            continue
        new_r = pl_r
        new_c = pl_c + 1

    elif move == "left":
        try:
            moving_to = matrix[pl_r][pl_c - 1]
        except IndexError:
            continue
        new_r = pl_r
        new_c = pl_c - 1

    if moving_to == "e":        # lose condition
        matrix[pl_r][pl_c] = "*"
        pl_r = new_r
        pl_c = new_c
        print(f"Game over! ({pl_r}, {pl_c})")
        lost = True
        break

    elif moving_to == "c":
        matrix[pl_r][pl_c] = "*"
        pl_r = new_r
        pl_c = new_c
        coal_on_field -= 1

        if coal_on_field == 0:  # win condition
            print(f"You collected all coal! ({pl_r}, {pl_c})")
            break

    else:
        matrix[pl_r][pl_c] = "*"
        pl_r = new_r
        pl_c = new_c


if coal_on_field > 0 and not lost:
    print(f"{coal_on_field} pieces of coal left. ({pl_r}, {pl_c})")
