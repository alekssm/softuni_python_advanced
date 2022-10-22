numbers = [float(x) for x in input().split()]

nums = {}

for number in numbers:
    if number not in nums:
        nums[number] = 0
    nums[number] += 1

for k, v in nums.items():
    print(f"{k} - {v} times")