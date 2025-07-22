class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("blu",10)
woo=parrot("woo",11)
print(f"the species of these parrots are {blu.species}")
print(f"{blu.name} is {blu.age} years old ")
print(f"{woo.name} is {woo.age} years old ")