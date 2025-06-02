

class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def  __str__(self):
        return str(self.name) + " - " + str(self.price)
    

class Phone(Product):
    def __init__(self,name,price,colour):
        Product.__init__(self,name,price)
        self.colour = colour

    def __str__(self):
        return super().__str__() + " - " + str(self.colour)
    

# phone1=Phone("iPhone 14", 999, "Black")
# print(phone1)

class TV(Product):
    def __init__(self,name,price,screen_size):
        Product.__init__(self,name,price)
        self.screen_size = screen_size 

    def __str__(self):
        return super().__str__() + " - " + str(self.screen_size) + " inches"

#tv1=TV("TV Y",2000,65)
#print(tv1)