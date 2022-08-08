class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = color,
        self.waist_size = waist_size,
        self.length = length,
        self.price = price
    
    def change_price(self, price):
        self.price = price

    def discount(self, parentage):
        return self.price * (1 - parentage)