num=int(input("enter a number below 20 :"))
numbers=[1,3,5,7,9,11,13,15,17,19]
odd=[x for x in numbers if x<num]
print(odd)