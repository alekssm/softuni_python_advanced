n = int(input())

elements = set()

for _ in range(n):
    els = input().split()
    for el in els:
        elements.add(el)

for e in elements:
    print(e)
