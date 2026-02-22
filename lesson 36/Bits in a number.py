def numberofbits(n):
    count=0
    while(n):
        count+=1
        n>>=1
    return count
num=int(input("enter a number"))
print("the number of bits is:",numberofbits(num))