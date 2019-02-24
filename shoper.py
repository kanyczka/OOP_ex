class Product():
    product_list = {}

    def check_code(code):
        if code in Product.product_list.keys():
            raise KeyError('Not a proper code! The code already in the base!')

    def __init__(self, code, name, price, weight):
        self.__code = code
        self.name = name
        self.price = price
        self.weight = weight
        Product.check_code(self.__code)
        if not isinstance(self.name, str):
            raise ValueError("Not a proper name!\nProduct wasn't added")
        if not isinstance(self.price, float):
            raise ValueError("Not a proper value!\nProduct wasn't added")
        if not isinstance(self.weight, float):
            raise ValueError("Not a proper value!\nProduct wasn't added")
        Product.product_list[self.__code] = (self.name, self.price, self.weight)

    def __str__(self):
        return "Produkt: " + self.__code + " - " + self.name

    def __repr__(self):
        return self.__code + ' - ' + self.name + ' - ' + str(self.price)

    @classmethod  # jaka jest różnica między staticmethod a classmethod
    def show_codes(cls):
        return Product.product_list.keys()

    @staticmethod
    def show_products():
        print(f"Lista utworzonych produktów (pozycji: {len(Product.product_list)})")
        no = 1
        for code, product in Product.product_list.items():
            print(f"{no}, {code}, {product}")
            no += 1


class Shop():

    def __init__(self, name="No name shop"):
        self.name = name
        self.products_in_shop = {}
        print(f"New shop was created: {name}\n")

    def __str__(self):
        return f"Shop's name: {self.name}\n"

    def add_product(self, product, quantity):
        self.product = product
        self.quantity = quantity
        if self.product not in self.products_in_shop:
            self.products_in_shop[self.product] = self.quantity
        else:
            raise KeyError(f"{self.product} already in the {self.name} shop!")

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

    def show_product(self, product):
        self.product = product
        self.quantity = self.products_in_shop.get(self.product, 'No such product')
        print(f"{self.product}, {self.quantity} szt")


class Cart():

    def __init__(self, capacity=15.00):
        self.products = {}
        self.capacity = capacity
        self.total_capacity = 0

    def add_product(self, product):
        self.product = product
        self.total_capacity += self.product.weight
        self.count = 1
        if self.total_capacity > self.capacity:
            raise ValueError("Not sufficient cart capacity")
        else:
            if product in self.products:
                # self.count += 1
                self.products[self.product] = self.count + 1
            else:
                self.products[self.product] = self.count

    def show_cart(self):
        for product, count in self.products.items():
            print(product, count)
        print(self.total_capacity)
