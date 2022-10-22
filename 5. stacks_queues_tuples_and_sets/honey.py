from collections import deque


def addition(numbers):
    return abs(sum(numbers))


def subtraction(numbers):
    return abs(numbers[0] - numbers[1])


def multiplication(numbers):
    return abs(numbers[0] * numbers[1])


def division(numbers):
    return abs(numbers[0] // numbers[1])


bees = deque(map(int, (input().split())))
nectar = list(map(int, input().split()))
operators = deque(input().split())

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

honey = 0

while bees and nectar:
    bee = bees[0]
    current_nectar = nectar.pop()

    if current_nectar < bee:
        continue
    else:
        current_operator = operators.popleft()
        honey += operations[current_operator]((bee, current_nectar))
        bees.popleft()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
