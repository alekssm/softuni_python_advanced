n = int(input())

even = set()
odd = set()

for i in range(1, n+1):
    name = input()
    current_name = 0

    for ch in name:
        current_name += ord(ch)

    current_name //= i
    if current_name % 2 == 0:
        even.add(current_name)
    else:
        odd.add(current_name)

if sum(odd) > sum(even):
    print(', '.join(str(x) for x in list(odd.difference(even))))
elif sum(even) > sum(odd):
    print(', '.join(str(x) for x in list(even.symmetric_difference(odd))))
else:
    print(', '.join(str(x) for x in list(even.union(odd))))
