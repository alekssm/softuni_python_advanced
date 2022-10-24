symbols = {"-", ",", ".", "!", "?"}

with open("text.txt", "r") as file:
    line_num = 0
    for line in file:
        if not line:
            break
        if not line_num % 2 == 0:
            line_num += 1
            continue
        for symbol in symbols:
            line = line.replace(symbol, "@")
        reversed_line = " ".join(reversed(line.split()))
        print(reversed_line)
        line_num += 1