list1=[4,1,90,8,5,6,13,9]
sum=0
for i in list1:
    sum+=i
avg=sum/len(list1)
print(f"the average of {sum} is {avg}")
list1.sort()
print(list1)
print("the smallest element is ",list1[0])
print("the largest element is ",list1[-1])
