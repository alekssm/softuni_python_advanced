import math
from collections import deque


def addition(numbers):
    return sum(numbers)


def subtraction(numbers):
    first = numbers[0]*2
    for number in numbers:
        first -= number
    return first


def multiplication(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def division(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result /= numbers[i]
    return math.floor(result)


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


info = deque(input().split())

current_numbers = []

while info:
    current_char = info.popleft()

    if current_char in operations:
        result = operations[current_char](current_numbers)
        current_numbers.clear()
        current_numbers.append(result)
    else:
        current_numbers.append(int(current_char))

print(current_numbers[0])
