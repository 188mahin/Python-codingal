#horsepower=hp
class BMW:
    def __init__(self,hp,speed):
        self.hp=hp
        self.speed=speed
    def printHp(self):
        return "the horsepower of the BMW is",self.hp
    def printSpeed(self):
        return "the maxspeed of the BMW is",self.speed
class Ferrari:
    def __init__(self,hp,speed):
        self.hp=hp
        self.speed=speed
    def printHp(self):
        return "the horsepower of the ferrari is",self.hp
    def printSpeed(self):
        return "the maxspeed of the ferrari is",self.speed

m4=BMW(503,250)
spider488=Ferrari(661,325)
for i in spider488,m4:
    print(i.printHp())
    print(i.printSpeed())