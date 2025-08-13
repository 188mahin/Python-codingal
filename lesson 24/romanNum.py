
romNum=input("enter a roman numeral:")
realnum=0
iterable=int(len(romNum))

for i in range(iterable):
    #for x in range(iterable):
    b=[]
    if romNum[i].lower()=="i":
                b.append(1)
    elif romNum[i].lower()=="v":
                b.append(5)
    elif romNum[i].lower()=="x":
                b.append(10)
    elif romNum[i].lower()=="l":
                b.append(50)
    elif romNum[i].lower()=="c":
                b.append(100)   
    elif romNum[i].lower()=="d":
                b.append(500)
    elif romNum[i].lower()=="m":
                b.append(1000)                               
    if romNum[i].lower()=="i":
            realnum+=1
    elif romNum[i].lower()=="v":
            realnum+=5  
    elif romNum[i].lower()=="x":
            realnum+=10
    elif romNum[i].lower()=="l":
            realnum+=50
    elif romNum[i].lower()=="c":
            realnum+=100
    elif romNum[i].lower()=="d":
            realnum+=500
    elif romNum[i].lower()=="m":
            realnum+=1000
    else:
        print("your roman numeral has a mistake,try again")
        
print(realnum)
print(b)