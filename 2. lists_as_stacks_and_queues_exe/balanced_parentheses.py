from collections import deque

text = input()

symbols = deque()

symbols_dd = {
    "{": "}",
    "[": "]",
    "(": ")",
}

for ch in text:
    symbols.append(ch)

if len(symbols) % 2 != 0:
    print("NO")

else:
    balanced = True

    while symbols:
        first = symbols[0]
        last = symbols[-1]
        if symbols_dd[first] != last:
            balanced = False
            break
        symbols.popleft()
        symbols.pop()

    if balanced:
        print("YES")
    else:
        print("NO")
