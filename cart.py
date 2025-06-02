

from products import *

class cart:
    def __init__(self):
        self.__productsList = []
        self.__cartValue = 0

    def addProduct(self, product): 
        if isinstance(product,Product): 
            if product not in self.__productsList:  
                self.__productsList.append(product)
                self.calculateCartValue()
            else:
                print("This product is already in the cart")
        else:
            print("This is not a product")
    def calculateCartValue(self):
        self.__cartValue = 0
        for el in self.__productsList:
            self.__cartValue += el.price
    def showCart(self):
        print("Products in the cart:")
        for el in self.__productsList:
            print(el.name)
        print("Total cart value:" + str(self.__cartValue) + "$")


phone = Phone("iPhone 14", 999, "Black")
tv = TV("TV Y", 2000, 65)



cart1 = cart()
cart1.addProduct(phone)
cart1.addProduct(tv)
cart1.showCart()

    
