try:
    age=int(input("enter a number:"))
    if age%2==0:
        print("age is even")
    else:
        print("age is odd")
except ValueError:
    print("number has to be integer type")
finally:
    print("error or not,this will print no matter what")

