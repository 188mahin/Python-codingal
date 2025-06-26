num=int(input("enter a number:"))
totaldigits=0
digit=num
while digit>0:
    digit//=10
    totaldigits+=1
print("the number of digits in your number are",totaldigits)