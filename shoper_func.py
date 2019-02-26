from shoper import Product, Shop, Cart


def go_on():
    input("======= Enter - kontynuacja programu =========")


def create_product(p):
    el_gener = (i for i in p)
    try:
        Product(next(el_gener), next(el_gener), next(el_gener), next(el_gener))
    except ValueError as err:
        print(err.args[0], '\n')
    except KeyError as err:
        print(err.args[0], '\n')
    else:
        print("Produkt dodano!\n")
    finally:
        print(Product.show_products())


def add_products_to_shop(shop, p, quantity):
    try:
        shop.add_product(p, quantity)
    except KeyError as err:
        print(err.args[0], '\n')
    else:
        print("\nDodano produkt\n")


def add_products_to_cart(cart, *args):
    print("\nDodawanie do koszyka: \n")
    try:
        cart.add_products(*args)
    except ValueError as err:
        print(err.args[0], '\n')
    else:
        print("Dodano produkty do koszyka\n")
    finally:
        print("Aktualnie w koszyku:")
        cart.show_cart()
