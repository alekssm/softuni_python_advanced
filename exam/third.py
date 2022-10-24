def shopping_list(budget, **kwargs):
    unique_products = 0
    products = {}
    if budget < 100:
        return "You do not have enough budget."
    else:
        for product, value in kwargs.items():
            price = value[0] * value[1]
            if price > budget:
                continue
            if product not in products:
                products[product] = 0
            products[product] = price
    list_of_bs = []
    for x, y in products.items():
        list_of_bs.append(f"You bought {x} for {y:.2f} leva.")
    return list_of_bs


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))