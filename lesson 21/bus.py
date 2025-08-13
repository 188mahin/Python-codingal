class Vehicle:
    def __init__(self,time,price):
        self.time=time
        self.price=price
class bus(Vehicle):
    def __init__(self, time, price):
        super().__init__(time, price)
    def fare(self):
        return self.price*self.time
obj=bus(3,1250)
print(obj.fare())