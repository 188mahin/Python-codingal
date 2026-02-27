num1=int(input("enter a number"))
num2=int(input("enter another number"))
num3=int(input("enter another number"))
d=num1&num2
e=num2|num3
f=num2&num3
g=f&e
x=d|g
print("the final output of the circuit is:",x)