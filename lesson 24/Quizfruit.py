import random
class FQ:
    def __init__(self):
        self.fruit={"apple":"red",
                    "orange":"orange",
                    "watermelon":"green",
                    "lemon":"yellow",
                    "Blueberry":"blue",
                                       }
    def quiz(self):
        while True:
            fruit,color=random.choice(list(self.fruit.items()))
            print(f'what is the color of the {fruit}')
            a=input()
            if a.lower()==color:
                print("correct answer")
            else:
                print("incorrect answer")
            option=int(input("enter 0 to continue else type 1:"))
            if (option):
                 break
print("welcome to FruitQuiz")
obj=FQ()
obj.quiz()