file = open("my_first_file.txt", "w")
file.write("I just created my first file")

with open("my_next_file", "w") as files:
    files.write("It's very nice")