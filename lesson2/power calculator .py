num=float(input("Enter a number"))
power=int(input("enter the number of times you want the number to be multiplyed by itself"))
product=1
for i in range(1,power+1):
    product=product*num
print(product)