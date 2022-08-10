class cloths:
    def __init__(self, color,size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price
    
    def calculate_discount(self, discount):
        return self.price * (1-discount)
    
    def calculate_shipping(self, weight, rate):
        return weight * rate

class shirt(cloths):
    def __init__(self, color, size, style, price, long_or_short):
        cloths.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short
    def double_price(self):
        self.price = 2*self.price

class Plants(cloths):
    def __init__(self, color, size, style, price, waist):
        cloths().__init__(color, size, style, price)
        self.waist = waist
    
    def calculate_discount(self, discount):
        return self.price * (1-discount / 2)

class Blouse(cloths):
    def __init__(self, color, size, style, price, country_of_origin):
        cloths().__init__(color, size, style, price)
        self.country_of_origin = country_of_origin
        
    def triple_price(self):
        return 3 * self.price