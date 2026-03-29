def powerof4(n):
    count=0
    if (n & (~(n &(n-1)))):
        while n>1:
            n>>=1
            count+=1
        if count%2==0:
            return True
        else:
            return False
num=int(input("enter a number"))
if powerof4(num):
    print("the number is a power of 4")
else:
    print("the number is not a power of 4")
        