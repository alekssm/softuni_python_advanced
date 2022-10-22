from collections import deque

chocolates = list(map(int, input().split(", ")))
cups_of_milk = deque(map(int, input().split(", ")))

milkshakes = 0

while chocolates and cups_of_milk:
    chocolate = chocolates[-1]
    if chocolate <= 0:
        chocolates.pop()
        continue
    milk = cups_of_milk.popleft()
    if milk <= 0:
        continue

    if chocolate == milk:
        milkshakes += 1
        chocolates.pop()

    else:
        chocolates[-1] -= 5
        cups_of_milk.append(milk)

    if milkshakes == 5:
        break

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")
