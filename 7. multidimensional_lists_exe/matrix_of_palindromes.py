n, m = map(int, input().split())

first_letter = ord("a")

matrix = []

for r in range(first_letter, first_letter+n):
    row = []
    for c in range(r, r+m):
        current_text = chr(r)+chr(c)+chr(r)
        row.append(current_text)
    matrix.append(row)

for row in matrix:
    print(' '.join(x for x in row))
