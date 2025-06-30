def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("choose your operation")
print("a.add\n")
print("b.subtract\n")
print("c.multiply\n")
print("d.divide\n")
choose=input("choose between a/b/c/d")
num1=int(input("enter a number"))
num2=int(input("enter another number"))
if choose=='a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choose=='b':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choose=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choose=='d':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid input")
