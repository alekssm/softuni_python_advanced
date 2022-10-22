n, m = map(int, input().split())

snake = input()

matrix = []

# for _ in range(n):
#     matrix.append([0] * m)

snake_idx = 0

for r in range(n):
    row = []
    for c in range(m):
        current_char = snake[snake_idx]
        row.append(current_char)
        snake_idx += 1
        if snake_idx == len(snake):
            snake_idx = 0
    if r == 0:
        matrix.append(row)
    elif r % 2 == 0:
        matrix.append(row)
    else:
        matrix.append(list(reversed(row)))

for row in matrix:
    print(''.join(str(x) for x in row))
