from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value = int(input())

used_bullets = 0
current_bullets = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    used_bullets += 1
    current_bullets += 1
    if current_bullet > current_lock:
        print("Ping!")
    else:
        print("Bang!")
        locks.popleft()
    if current_bullets == barrel_size and bullets:
        print("Reloading!")
        current_bullets = 0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value - used_bullets * bullet_price}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")