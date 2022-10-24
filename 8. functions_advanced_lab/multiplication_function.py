def multiply(*args):
    multiply_sum = 1
    for num in args:
        multiply_sum *= num
    return multiply_sum


print(multiply(4, 5, 6, 1, 3))