class shirt:
    def __init__(self, color, size, style, price):
        self.color = color,
        self.size = size,
        self.style = style,
        self.price = price
    
    def change_price(self, price):
        self.price = price
        
    def discount(self, dic):
        return self.price*dic