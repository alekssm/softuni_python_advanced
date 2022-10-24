import math

player_one, player_two = input().split(", ")
n = 7

matrix = []

for _ in range(n):
    row = input().split()
    matrix.append(row)

first_score = 501
second_score = 501

player_turn = 1
turn = 0

while first_score > 0 and second_score > 0:
    turn += 1
    if player_turn == 3:
        player_turn = 1

    hit = input()
    hit = [int(x) for x in hit[1:-1].split(", ")]
    hit_row = hit[0]
    hit_col = hit[1]

    if hit_row >= n or hit_row < 0 or hit_col >= n or hit_col < 0:
        player_turn += 1
        continue

    target_hit = matrix[hit_row][hit_col]
    if target_hit == "B":
        if player_turn == 1:
            first_score = 0
            break
        else:
            second_score = 0
            break
    elif target_hit == "D":
        score = (int(matrix[hit_row][0]) + int(matrix[hit_row][n-1]) + int(matrix[0][hit_col]) + int(matrix[n-1][hit_col])) * 2
        if player_turn == 1:
            first_score -= score
        else:
            second_score -= score
    elif target_hit == "T":
        score = (int(matrix[hit_row][0]) + int(matrix[hit_row][n-1]) + int(matrix[0][hit_col]) + int(matrix[n-1][hit_col])) * 3
        if player_turn == 1:
            first_score -= score
        else:
            second_score -= score
    else:
        if player_turn == 1:
            first_score -= int(target_hit)
        else:
            second_score -= int(target_hit)

    player_turn += 1

if first_score <= 0:
    print(f"{player_one} won the game with {math.ceil(turn/2)} throws!")
else:
    print(f"{player_two} won the game with {math.floor(turn/2)} throws!")