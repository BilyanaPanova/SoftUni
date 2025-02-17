def dict_stocks():
    products = input().split()
    product, quantities = products[::2], [int(x) for x in products[1::2]]
    stock = dict(zip(product, quantities))
    return stock


def print_el():
    dict_stock = dict_stocks()
    searched_products = input().split()

    for searched_product in searched_products:
        if searched_product in dict_stock.keys():
            print(f"We have {dict_stock[searched_product]} of {searched_product} left")
        else:
            print(f"Sorry, we don't have {searched_product}")


if __name__ == "__main__":
    print_el()