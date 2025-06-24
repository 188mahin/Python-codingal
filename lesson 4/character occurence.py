string=input("enter a word:")
char=input("enter your character:")
i=0
count=0
while i<len(string):
    if string[i]== char:
        count+=1
    i+=1
print("the number of times your character has appeared is",count)

