from collections import deque

food = int(input())
orders = deque(map(int, input().split()))

biggest_order = max(orders)

while orders:

    if food - orders[0] >= 0:
        food -= orders[0]
        orders.popleft()
    else:
        break

print(biggest_order)

if orders:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")
else:
    print("Orders complete")



