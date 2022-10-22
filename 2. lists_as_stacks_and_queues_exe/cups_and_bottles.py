from collections import deque

cups_capacity = deque(map(int, input().split()))
bottle_capacity = list(map(int, input().split()))

wasted_water = 0


while cups_capacity and bottle_capacity:
    current_bottle = bottle_capacity.pop()
    current_cup = cups_capacity[0]

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups_capacity.popleft()

    else:
        cups_capacity[0] -= current_bottle

if not cups_capacity:
    print(f"Bottles: {' '.join(str(x) for x in bottle_capacity)}")
    print(f"Wasted litters of water: {wasted_water}")
else:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
    print(f"Wasted litters of water: {wasted_water}")
