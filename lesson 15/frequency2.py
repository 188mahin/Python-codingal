dict1={"coding1":1,"coding2":2,"coding3":3,"coding4":1}
num=int(input("enter a number batween 1 or 3:"))
count=1
for value in dict1.items():
    if num==value:
        count+=1
print(f"the frequency of {num} is {count}")


