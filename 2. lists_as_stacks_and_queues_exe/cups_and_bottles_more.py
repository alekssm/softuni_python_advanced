from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted_water = 0

while cups and bottles:
    cup = cups[0]
    while cup > 0 and bottles:
        bottle = bottles.pop()
        if cup - bottle > 0:
            cup -= bottle
        else:
            cups.popleft()
            wasted_water += bottle - cup
            break
if not cups:
    print(f"Bottles: {' '.join(map(str, bottles))}")
elif not bottles:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")