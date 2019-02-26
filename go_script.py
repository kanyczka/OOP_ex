from shoper import Product, Shop, Cart
from shoper_func import *


def main():
    print("\n1. Tworzę kilka produktów... \n")
    p1 = Product("tv_sam_s23", "Samsung S23 tv set", 1000.00, 3.00)
    p2 = Product("phone_lgv30", "Smartphone LG V30", 3000.00, 0.2)
    p3 = Product("tv_sam_s21", "SamsungS21 tv set", 990.00, 3.00)
    p4 = Product("phone_s23", "Smartphone Samsung SG33", 2500.00, 0.2)
    p5 = Product("phone_htc10", "Smartphone HTC 10", 2700.00, 0.2)
    print(Product.show_products())

    print("\n2.a. Próba dodania produktu z istniejącym już kodem:\n")
    p = ["phone_htc10", "Smartphone HTC 10", 2700.00, 0.2]
    create_product(p)
    go_on()

    print("\n2.b. Próba dodania produktu ze złym typem danych w polu Price:\n")
    p = ["ble", "Ble", 'aaaa', 0.2]
    create_product(p)
    go_on()

    print("\n2.c. Próba dodania nowego produktu z prawidłowymi danymi:\n")
    p = ["latitude e7470", "Laptop Dell", 3000.00, 1.0]
    print(p)
    create_product(p)
    go_on()

    # Utworzenie nowego sklepu
    print("\n3. Tworzenie nowego sklepu")
    shop_name = input("Podaj nazwę sklepu: ")
    new_shop = Shop(shop_name)

    # Dodanie produktów do sklepu
    new_shop.add_product(p1, 10)
    new_shop.add_product(p2, 20)
    new_shop.add_product(p3, 15)

    # Lista produktów w sklepie
    print(f"4. Do sklepu {new_shop.name} dodano następujące produkty: \n")
    new_shop.show_products_list()

    # Próba dodania tego samego produktu
    print("\n4.a Próbujemy dodać istniejący już w sklepie produkt\n")
    add_products_to_shop(new_shop, p1, 20)
    go_on()

    # Próba dodania nowego produktu
    print("\n4.b Próbujemy dodać nowy produkt do sklepu\n")
    print(p4.__repr__())
    add_products_to_shop(new_shop, p4, 20)
    go_on()

    # Zmiana ilości produktów
    print("\n5. Próbujemy zmienić pole quantity w jednym z produktów w sklepie\n")
    new_shop.show_product(p1)
    new_quantity = 20
    product = p1
    print(f"\nZmieniamy ilość na {new_quantity} szt")
    new_shop.change_quantity(product, new_quantity)
    print("\nAktualna lista produktów w sklepie: ")
    new_shop.show_products_list()
    go_on()

    # Utworzenie koszyka
    print("\nNowy koszyk. Dodajemy produkty.\n")
    cart_1 = Cart(9.00)
    add_products_to_cart(cart_1, p1, p2)
    add_products_to_cart(cart_1, p2, p3, p1)
    add_products_to_cart(cart_1, p2)
    go_on()


if __name__ == "__main__":
    main()
