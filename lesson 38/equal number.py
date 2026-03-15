def checkifnumberisequal(a,n):
    if((a^n)==0):
        print("the numbers are same")
    else:
        print("the numbers are different")
num=int(input("enter a number"))
num2=int(input("enter another number"))
checkifnumberisequal(num,num2)