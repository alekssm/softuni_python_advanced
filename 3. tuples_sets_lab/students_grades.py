def average(val):
    return sum(val) / len(val)


number_of_students = int(input())

students = {}

for _ in range(number_of_students):
    info = input().split()
    name = info[0]
    grade_str = info[1]
    grade = float(grade_str)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for k, v in students.items():
    avg = average(v)
    grades_str = ' '.join(str(f"{x:.2f}") for x in v)
    print(f"{k} -> {grades_str} (avg: {avg:.2f})")

#for k, v in students.items():
#    grades = list(map(float, v))
#    avg = 0
#    for g in grades:
#        avg += g
#    avg = avg / len(grades)
#    print(f"{k} -> {' '.join(v)} (avg: {avg:.2f})")