rowsize=int(input("enter the number of rows"))
if rowsize%2==0:
    halfdiamrows=int(rowsize/2)
else:
    halfdiamrows=int(rowsize/2)+1
space=halfdiamrows-1
for i in range(1,halfdiamrows+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num+=1
    print()

