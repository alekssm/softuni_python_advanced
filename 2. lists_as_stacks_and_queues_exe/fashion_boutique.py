from collections import deque

clothes = deque(map(int, input().split()))
rack_size = int(input())

number_of_racks = 1
current_rack = 0

while clothes:
    current_cloth = clothes[0]

    if current_rack + current_cloth <= rack_size:
        current_rack += current_cloth
        clothes.popleft()
    else:
        number_of_racks += 1
        current_rack = current_cloth
        clothes.popleft()

print(number_of_racks)
