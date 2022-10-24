punctuation_marks = {"-", ",", ".", "!", "?", "'", '"', "-", "_", ":", ";", "...", "(", ")"}

with open("text.txt", "r") as file, open("result.txt", "w") as result:
    line_num = 1
    for line in file:
        letter_count = 0
        punctuation_mark_count = 0
        for char in line:
            if char.isalpha():
                letter_count += 1
            elif char in punctuation_marks:
                punctuation_mark_count += 1
        result.write(f"Line {line_num}: {line.strip()} ({letter_count})({punctuation_mark_count})\n")
        line_num += 1