from collections import deque

mats = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0

while mats and magic_levels:

    magic = magic_levels.popleft()
    mat = mats.pop()

    result = magic + mat

    if 100 <= result <= 499:
        if 100 <= result <= 199:
            gemstone += 1
        elif 200 <= result <= 299:
            porcelain_sculpture += 1
        elif 300 <= result <= 399:
            gold += 1
        elif 400 <= result <= 499:
            diamond_jewellery += 1
    else:
        if result < 100 and result % 2 == 0:
            result = mat*2 + magic*3
            if not 100 <= result <= 499:
                continue
            else:
                if 100 <= result <= 199:
                    gemstone += 1
                elif 200 <= result <= 299:
                    porcelain_sculpture += 1
                elif 300 <= result <= 399:
                    gold += 1
                elif 400 <= result <= 499:
                    diamond_jewellery += 1
        elif result < 100 and result % 2 != 0:
            result *= 2
            if not 100 <= result <= 499:
                continue
            else:
                if 100 <= result <= 199:
                    gemstone += 1
                elif 200 <= result <= 299:
                    porcelain_sculpture += 1
                elif 300 <= result <= 399:
                    gold += 1
                elif 400 <= result <= 499:
                    diamond_jewellery += 1
        elif result > 499:
            result /= 2
            if not 100 <= result <= 499:
                continue
            else:
                if 100 <= result <= 199:
                    gemstone += 1
                elif 200 <= result <= 299:
                    porcelain_sculpture += 1
                elif 300 <= result <= 399:
                    gold += 1
                elif 400 <= result <= 499:
                    diamond_jewellery += 1


if (gemstone and porcelain_sculpture) or (gold and diamond_jewellery):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if mats:
    print(f"Materials left: {', '.join(str(x) for x in mats)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

if diamond_jewellery:
    print(f"Diamond Jewellery: {diamond_jewellery}")
if gemstone:
    print(f"Gemstone: {gemstone}")
if gold:
    print(f"Gold: {gold}")
if porcelain_sculpture:
    print(f"Porcelain Sculpture: {porcelain_sculpture}")
