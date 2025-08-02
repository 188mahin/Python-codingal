class Computer:
    def __init__(self):
        self.__max_price=1000
    def sell(self):
        print("The selling price is",self.__max_price)
    def SetMaxPrice(self,price):
        self.__max_price=price
obj=Computer()
obj.sell()
obj.__max_price=920
obj.sell()
obj.SetMaxPrice(890)
obj.sell()