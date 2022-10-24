def func_executor(*args):
    result = []
    for arg in args:
        result.append(arg[0](*arg[1]))
    return result


# def sum_numbers(*args):
#     return sum(args)
#
#
# def multiply_numbers(*args):
#     result = 1
#     for arg in args:
#         result *= arg
#     return result

def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
