def twooddnumber(arr,size):
    xoroftwo=arr[0]
    x=0
    y=0
    Setbit=0
    for i in range(1,size):
        xoroftwo=xoroftwo^arr[i]
    Setbit=xoroftwo&~(xoroftwo-1)
    for i in range(size):
        if arr[i]&Setbit:
            x=x^arr[i]
        else:
            y=y^arr[i]
    print("the 2 odd elements are:", x,"and",y)
arr=[]
size=int(input("enter the size of the array"))
n=size
while(size):
    num=int(input("enter a number"))
    arr.append(num)
    size-=1
twooddnumber(arr,n)