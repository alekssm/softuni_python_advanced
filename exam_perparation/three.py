def stock_availability(cupcakes, command, *args):
    if command == "delivery":
        for flavour in args:
            cupcakes.append(flavour)
        return cupcakes
    elif command == "sell":
        if not args:
            cupcakes.pop(0)
            return cupcakes
        elif str(args[0]).isdigit():
            for box in range(args[0]):
                cupcakes.pop(0)
            return cupcakes
        else:
            for flavour in args:
                if flavour in cupcakes:
                    cupcakes = [item for item in cupcakes if not item == flavour]
            return cupcakes


print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))