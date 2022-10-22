from collections import deque

number_of_pumps = int(input())

runs = deque()

for i in range(number_of_pumps):
    petrol, distance = list(map(int, input().split()))

    runs.append((petrol, distance))

for ind in range(len(runs)):
    complete = True
    gas_left = 0

    for run in runs:
        gas = run[0]
        distance = run[1]

        gas_left += gas
        if gas_left - distance < 0:
            complete = False
            break

    if complete:
        print(ind)
        break
    else:
        runs.append(runs.popleft())
