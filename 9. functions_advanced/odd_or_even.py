command = input()
nums = [int(x) for x in input().split()]

parity = 0 if command == "Even" else 1

result = sum(x for x in nums if x % 2 == parity) * len(nums)

print(result)
