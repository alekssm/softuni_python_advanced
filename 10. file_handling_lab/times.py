file = open("words.txt", "r")
file_two = open("text.txt")

list_one = file.readline().lower().split()
list_two = ""
while True:
    line = file_two.readline().lower()
    list_two += line
    if not line:
        break
new_list_two = ""
for s in list_two:
    if s.isalpha() or s == " ":
        new_list_two += s
    else:
        s = " "
        new_list_two += s

results = {}

new_list_two = new_list_two.split()

for item in list_one:
    if item not in results:
        results[item] = 0
    for word in new_list_two:
        if word == item:
            results[item] += 1

sort_results = sorted(results.items(), key=lambda kvp: -kvp[1])
for k, v in sort_results:
    print(f"{k} - {v}")