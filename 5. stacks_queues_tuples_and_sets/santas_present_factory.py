from collections import deque

gifts = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted = {}

mats = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

while mats and magic_level:
    mat = mats[-1]
    if mat == 0:
        mats.pop()
        continue
    magic = magic_level.popleft()

    if magic == 0:
        continue

    result = mat * magic

    if result < 0:
        new_mat = mat + magic
        mats.pop()
        mats.append(new_mat)

    else:
        if result in gifts:
            mats.pop()
            if gifts[result] not in crafted:
                crafted[gifts[result]] = 0
            crafted[gifts[result]] += 1
        else:
            mats[-1] += 15

if ("Doll" in crafted and "Wooden train" in crafted) or ("Teddy bear" and "Bicycle") in crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if mats:
    print(f"Materials left: {', '.join((str(x) for x in reversed(mats)))}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for (k, v) in sorted(crafted.items(), key=lambda kvp: kvp[0]):
    print(f"{k}: {v}")
