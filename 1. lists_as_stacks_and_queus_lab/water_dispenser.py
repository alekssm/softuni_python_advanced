from collections import deque
liters = int(input())

deq = deque()
com = input()

while not com == "Start":
    deq.append(com)
    com = input()

com = input()

while not com == "End":
    if "refill" in com:
        ll = com.split()
        liters += int(ll[1])
    else:
        if int(com) <= liters:
            print(f"{deq.popleft()} got water")
            liters -= int(com)
            if liters < 0:
                liters = 0
        else:
            print(f"{deq.popleft()} must wait")
    com = input()

print(f"{liters} liters left")