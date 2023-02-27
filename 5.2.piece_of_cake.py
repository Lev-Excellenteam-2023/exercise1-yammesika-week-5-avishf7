def get_recipe_price(dict_prices, optionals = None, **dict_weight):
    """
    Calculate the total price of a recipe based on the ingredient prices and their weights.
    :param dict_prices: A dictionary where keys are ingredient names and values are their prices.
    :param optionals: A list of optional ingredients to exclude from the recipe.
    :param dict_weight: Keyword arguments where keys are ingredient names and values are their weights in grams.
    :return: The total price of the recipe, or 0 if not all ingredients are included in both `dict_prices` and
             `dict_weight`.
    """
    prices = {}
    prices.copy(dict_prices)

    if optionals:
        for ingredient in optionals:
            del prices[ingredient]

    if prices.keys() != dict_weight.keys():
        print("ERROR: not all ingredients include!")
        return 0
    else:
        sum_price = 0.0
        for ingredient in dict_prices:
            sum_price += prices[ingredient] * (dict_weight[ingredient] / 100)

        return sum_price
