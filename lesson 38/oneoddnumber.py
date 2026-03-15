def oddnumber(arr):
    res=0
    for i in arr:
        res=res^i
    return res
arr=[]
size=int(input("enter the size of the array"))
while(size):
    num=int(input("enter a number"))
    arr.append(num)
    size-=1
print("the odd occuring number in your array is:",oddnumber(arr))
