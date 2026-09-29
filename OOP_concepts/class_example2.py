
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_brand(self):
        return self.brand

    def set_brand(self, NewBrand):
        self.brand = NewBrand

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


m1 = Mobile("Samsung", 20000)
m2 = Mobile("iphone", 80000)

m1.display()
m2.display()

print("Old Price:", m1.get_price())

m1.set_price(25000)

print("New Price:", m1.get_price())