from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value = int(input())

out_of_ammo = False

bullets_used = 0

current_bullets = 0

while True:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
        bullets_used += 1
        current_bullets += 1
    else:
        print("Ping!")
        bullets_used += 1
        current_bullets += 1

    if not bullets:
        out_of_ammo = True
        break

    if current_bullets == gun_barrel_size:
        current_bullets = 0
        print("Reloading!")

    if not locks:
        break

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value - (bullet_price * bullets_used)}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

