def factorial(n):
    print(f"cal fact {n}")
    if n == 0 or n == 1:
        return 1

    result = n * factorial(n -1)
    print(result)
    return result


factorial(5)