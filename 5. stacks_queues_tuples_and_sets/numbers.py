first = set(map(int, input().split()))
second = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command = input().split()

    if "First" in command and "Add" in command:
        numbers = list(map(int, command[2:]))

        first.update(numbers)

    elif "Second" in command and "Add" in command:
        numbers = list(map(int, command[2:]))

        second.update(numbers)

    elif "First" in command and "Remove" in command:
        numbers = list(map(int, command[2:]))

        first = first.difference(numbers)

    elif "Second" in command and "Remove" in command:
        numbers = list(map(int, command[2:]))

        second = second.difference(numbers)

    else:
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")

print(f"{', '.join(sorted(str(x) for x in first))}")
print(f"{', '.join(sorted(str(x) for x in second))}")
