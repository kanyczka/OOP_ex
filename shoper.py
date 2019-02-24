class Product():

    product_list = {}

    def check_code(code):
        if code in Product.product_list.keys():
            raise KeyError('Kod musi być unikalny!')

    def __init__(self, code, name, price, weight):
        self.__code = code
        self.name = name
        self.price = price
        self.weight = weight
        Product.check_code(self.__code)
        if not isinstance(self.name, str):
            raise ValueError("Not a proper name")
        if not isinstance(self.price, float):
            raise ValueError("Not a proper value")
        if not isinstance(self.weight, float):
            raise ValueError("Not a proper value")
        Product.product_list[self.__code] = (self.name, self.price, self.weight)

    def __str__(self):
        return "Produkt: " + self.__code + " - " + self.name


    # @staticmethod
    # def show_codes():
    #     print(Product.products_codes)

    @classmethod            # jaka jest różnica między staticmethod a classmethod
    def show_codes(cls):
        return Product.product_list.keys()

    @staticmethod
    def show_products():
        print(f"Utworzono {len(Product.product_list)} produktów:")
        no = 1
        for code, product in Product.product_list.items():
            print(f"{no}, {code}, {product}")
            no += 1


class Shop():

    def __init__(self, name="No name shop"):
        self.name = name
        self.products_in_shop = {}
        print(f"Stworzono nowy sklep: {name}\n")

    def __str__(self):
        return f"Nazwa sklepu: {self.name}\n"


    def add_product(self, product, quantity):
        self.product = product
        self.quantity = quantity
        if self.product not in self.products_in_shop:
            self.products_in_shop[self.product] = self.quantity
        else:
            raise ValueError(f"{self.product} został już dodany do sklepu!")

            # print(f"{self.product} znajduje się już w sklepie!\nProduktu nie dodano")

    def change_quantity(self, product, quantity):
        self.product = product
        self.quantity = quantity
        if self.product in self.products_in_shop:
            self.products_in_shop[self.product] = self.quantity
        else:
            print("Brak takiego produktu w sklepie!")


    def show_products_list(self):
        for self.product, self.quantity in self.products_in_shop.items():
            print(f"{self.product}, ilość: {self.quantity}")











