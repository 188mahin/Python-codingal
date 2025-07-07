import random
playing=True
number=str(random.randint(10,20))
print("you have to guess a number between 10 and 20")
while playing:
    num=str(input("enter a number between 10 and 20:"))
    if num==number:
        print("your guess is correct")
        print(f"the number was {number}")
        break
    else:
        print("your guess is incorect try again")

    