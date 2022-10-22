a, b = list(map(int, input().split()))

first = set()
second = set()

for _ in range(a):
    first.add(int(input()))

for _ in range(b):
    second.add(int(input()))

both = first.intersection(second)
for item in both:
    print(item)
