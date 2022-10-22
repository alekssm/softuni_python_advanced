from collections import deque
names = input().split()
names_queue = deque()
for p in names:
    names_queue.append(p)
num = int(input())

while names_queue:
    for _ in range (num - 1):
        names_queue.append(names_queue.popleft())
    out = names_queue.popleft()
    if names_queue:
        print(f"Removed {out}")
    else:
        print(f"Last is {out}")