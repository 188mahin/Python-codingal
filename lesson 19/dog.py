class dog:
    def __init__(self,breed,age):
        self.breed=breed
        self.age=age
milo=dog('german shephard',7)
snowy=dog('shitzu',9)
print(f"the dog snowy's age is {snowy.age} and its breed is {snowy.breed}")
print(f"the dog milo's age is {milo.age} and its breed is {milo.breed}")