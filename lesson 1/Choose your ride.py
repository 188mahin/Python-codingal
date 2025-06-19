print("select your ride")
print("1.Bike")
print("2.Car")
choice=int(input("enter your choice:"))
if choice==1:
    print("what type of bike")
    print("1.Scooty")
    print("2.Scooter")
    choice_1=int(input("enter your choice:"))
    if choice_1==1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")
elif choice==2:
    print("what type of car")
    print("1.Sedan")
    print("2.XUV")
    choice_2=int(input("enter your choice:"))
    if choice_2==1:
        print("you have selected sedan")
    else:
        print("you have selected XUV")
else:
    print("incorrect input.Try again")