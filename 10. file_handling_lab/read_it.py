file = open("numbers.txt", "r")


sum_of_nums = 0
for f in file:
    num = int(f)
    sum_of_nums += num

print(sum_of_nums)