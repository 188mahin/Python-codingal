num=int(input("enter a number:"))
t=num
numlen=0
while t>0:
    numlen+=1
    t//=10
if numlen>=4:
    numlen=int(numlen/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numlen:
            midone=rem
        elif chk==(numlen-1):
            midtwo=rem
        num=int(num/10)
        chk+=1
    prod=midone*midtwo
    print("the product of the middle numbers of your number is",prod)
else:
    print("enter four or more number of digits")




