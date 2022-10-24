def age_assignment(*args, **kwargs):
    result = {}
    for arg in args:
        for kwarg in kwargs:
            if arg[0] == kwarg:
                result[arg] = kwargs[kwarg]
    return result

print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
