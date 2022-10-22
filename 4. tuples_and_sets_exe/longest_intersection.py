n = int(input())

longest_intersection = []

for _ in range(n):
    first, second = input().split("-")
    a, b = list(map(int, first.split(",")))
    c, d = list(map(int, second.split(",")))

    f = set(x for x in range(a, b+1))
    s = set(x for x in range(c, d+1))

    int_f_s = f.intersection(s)
    if len(int_f_s) > len(longest_intersection):
        longest_intersection = int_f_s

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
