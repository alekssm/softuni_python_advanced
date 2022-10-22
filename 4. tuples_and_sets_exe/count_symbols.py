text = input()

characters = {}

for ch in text:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1

for (k, v) in sorted(characters.items(), key=lambda kvp: ord(kvp[0])):
    print(f"{k}: {v} time/s")
