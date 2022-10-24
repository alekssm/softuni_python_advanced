def fill_the_box(*args):
    height, length, width = args[:3]
    volume = height * length * width
    cubes = []
    for x in args[3:]:
        if x == "Finish":
            break
        cubes.append(x)

    result = volume - sum(cubes)
    if result > 0:
        return f"There is free space in the box. You could put {result} more cubes."
    else:
        return f"No more free space! You have {abs(result)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
