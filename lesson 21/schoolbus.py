class vehicle:
    def __init__(self,name,maxSpeed,mileage):
        self.name=name
        self.maxSpeed=maxSpeed
        self.mileage=mileage
class bus(vehicle):
    pass
schoolBus=bus('Volvo',150,14)
print('name:',schoolBus.name,'Max speed:',schoolBus.maxSpeed,'Mileage:',schoolBus.mileage)
