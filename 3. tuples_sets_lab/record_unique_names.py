num = int(input())

names = []

for _ in range(num):
    name = input()
    names.append(name)

unique = set(names)
while unique:
    print(unique.pop())