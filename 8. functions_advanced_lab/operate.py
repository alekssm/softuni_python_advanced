def operate(operator, *args):
    result = 0
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
    elif operator == "*":
        result = 1
        for i in range(0, len(args)):
            result *= args[i]
    elif operator == "/":
        result = args[0]
        for i in range(1, len(args)):
            if args[i] == 0:
                continue
            result /= args[i]
    return result


print(operate("/", 0))