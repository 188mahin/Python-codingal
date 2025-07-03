num=int(input("enter a number:"))
num2=int(input("enter another number:"))
num3=int(input("enter the third number:"))
def number():
    if num > num2 and num > num3:
        return num
    elif num2 > num and num2 > num3:
        return num2
    else:
        return num3
print(number())