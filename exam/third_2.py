def shopping_list(budget, **kwargs):
    products = []
    result = []
    if budget < 100:
        return "You do not have enough budget."
    else:
        for product, value in kwargs.items():
            price = value[0] * value[1]
            if price > budget:
                continue
            result.append(f"You bought {product} for {price:.2f} leva.")
            if product not in products:
                products.append(product)
            if len(products) == 5:
                return "\n".join(result)
            budget -= price
    return "\n".join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))