from shoper import Product, Shop


def main():

    def go_on():
        input("Enter - kontynuacja programu")

    def create_product(p, msg):
        el_gener = (i for i in p)
        try:
            print(f"\n{msg}\n")
            Product(el_gener, el_gener, el_gener, el_gener)
        except ValueError as err:
            print(err.args[0], '\n')
        except KeyError as err:
            print(err.args[0], '\n')
        finally:
            print(Product.show_products())

    print("\nTworzę kilka produktów... \n")
    p1 = Product("tv_sam_s23", "Samsung S23 tv set", 1000.00, 3.00)
    p2 = Product("phone_lgv30", "Smartphone LG V30", 3000.00, 0.2)
    p3 = Product("tv_sam_s21", "SamsungS21 tv set", 990.00, 3.00)
    p4 = Product("phone_s23", "Smartphone Samsung SG33", 2500.00, 0.2)
    p5 = Product("phone_htc10", "Smartphone HTC 10", 2700.00, 0.2)

    msg = "Próba dodania produktu z istniejącym już kodem\n"
    p = ["phone_htc10", "Smartphone HTC 10", 2700.00, 0.2]

    create_product(p, msg)

    # try:
    #     print("\nPróba dodania produktu z tym samym kodem... \n")
    #     Product("tv_sam_s23", "Samsung S23 tv set", 1000.00, 3.00)
    # except ValueError as err:
    #     print(err.args[0], '\n')
    # except KeyError as err:
    #     print(err.args[0], '\n')
    # finally:
    #     print(Product.show_products())

    go_on()

    # Utworzenie nowego sklepu
    print("\nTworzenie nowego sklepu")
    shop_name = input("Podaj nazwę sklepu: ")
    new_shop = Shop(shop_name)

    # Dodanie produktów do sklepu
    new_shop.add_product(p1, 10)
    new_shop.add_product(p2, 20)
    new_shop.add_product(p3, 15)

    # Lista produktów w sklepie
    print(f"W sklepie {new_shop.name} są następujące produkty: \n")
    new_shop.show_products_list()


    # Próba dodania tego samego produktu
    print("\nPróbujemy dodać istniejący już w sklepie produkt")
    try:
        new_shop.add_product(p3, 20)
    except ValueError("Produkt istnieje już w sklepie!\n"):
        print("Produkt nie został dodany")
    else:
        print("Dodano produkt")

    # Zmiana ilości produktów
    new_quantity = 20
    product = p1
    print(f"\nZmieniamy ilość jednego z produktów w sklepie: {product} na {new_quantity} szt")
    new_shop.change_quantity(product, new_quantity)
    print("\nAktualna lista produktów w sklepie: ")
    new_shop.show_products_list()





if __name__ == "__main__":
    main()

