lowRange=int(input("enter the lower range:"))
upperRange=int(input("enter the upper range:"))
list1=[]
for i in range(lowRange,upperRange+1):
    square=i*i
    list1.append(square)
    print(square)
    if square%2==0:
        print("the square of the number is even")
    else:
        print("the square of the number is odd")
print("all the squares are presented in the list",list1)
sum1=sum(list1)
avg=sum1/((upperRange-lowRange)+1)
print(f"the avg of the squares between {lowRange} and {upperRange} is {avg}")

    