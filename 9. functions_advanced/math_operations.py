from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(x for x in args)
    dd = kwargs
    idx = 1

    while nums:
        num = nums.popleft()
        if idx == 1:
            dd["a"] += num
        elif idx == 2:
            dd["s"] -= num
        elif idx == 3:
            if num == 0:
                pass
            else:
                dd["d"] /= num
        elif idx == 4:
            dd["m"] *= num

        idx += 1
        if idx == 5:
            idx = 1

    return dd


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
