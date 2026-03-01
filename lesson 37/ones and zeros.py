def onesandzeros(n):
    
    countofones=0
    countofzeros=0
    while n:
        if n&1==1:
            countofones+=1
        else:
            countofzeros+=1
        n>>=1
    print("the number of zeros is:",countofzeros)
    print("the number of ones in:",countofones)
number=int(input("enter a number:"))
onesandzeros(number)
