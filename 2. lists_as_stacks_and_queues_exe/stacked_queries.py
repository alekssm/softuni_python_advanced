n = int(input())

nums = []

for i in range(n):
    query = input().split()

    if query[0] == '1':
        nums.append(int(query[1]))

    elif query[0] == '2':
        if nums:
            nums.pop()

    elif query[0] == '3':
        if nums:
            print(max(nums))

    elif query[0] == '4':
        if nums:
            print(min(nums))

print(", ".join(reversed([str(x) for x in nums])))