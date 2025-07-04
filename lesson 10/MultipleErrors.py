try:
    num1,num2=eval(input("enter two numbers seprated by a comma:"))
    result=num1/num2
    print(f"the result is {result}")
except ZeroDivisionError:
    print("division by 0 is error")
except SyntaxError:
    print("please add a comma to seprate the numbers while giving the input like 1,2")
except:
    print("enter numbers divisible by ten only")
else:
    print("perfect input, zero errors")
finally:
    print("this will print no matter what")
