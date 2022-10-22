num = input().split()
reversed_numbers = []

for i in range(len(num)):
    reversed_numbers.append(num.pop())

print(" ".join(reversed_numbers))
