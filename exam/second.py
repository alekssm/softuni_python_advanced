n = 6

matrix = []

for _ in range(n):
    row = input().split()
    matrix.append(row)

points = 0

turns = 0

while not turns == 3:
    hit = input()
    hit = [int(x) for x in hit[1:-1].split(", ")]
    hit_row = hit[0]
    hit_col = hit[1]

    if hit_row >= n or hit_row < 0 or hit_col >= n or hit_col < 0:
        turns += 1
        continue

    target_hit = matrix[hit_row][hit_col]
    if not target_hit == "B":
        turns += 1
        continue
    else:
        points_down = 0
        points_up = 0
        for indx in range(hit_row + 1, n):
            points_down += int(matrix[indx][hit_col])
        for indx in range(hit_row - 1, -1, -1):
            points_up += int(matrix[indx][hit_col])
        points += (points_down + points_up)
        matrix[hit_row][hit_col] = "X"
    turns += 1

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif points < 200:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif points < 300:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")