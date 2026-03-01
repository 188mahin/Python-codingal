def setornot(number,n):
    
    if number%(1<<(n-1)):
        print("the number is a set")
    else:
        print("the number is not a set")
num=int(input("enter a number:"))
n=int(input("enter the position of the bit to check if it is set or not"))
setornot(num,n)
