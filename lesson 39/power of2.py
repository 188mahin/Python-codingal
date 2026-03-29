def powerof2(n):
    if n==0:
        return 0
    if (~(n-1))&(n)==n:
        return 1
    return 0
num=int(input("enter a number"))
if powerof2(num):
    print("the number is a power of 2")
else:
    print("the number is a not power of 2")