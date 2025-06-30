num=int(input("enter a number:"))
n=0
t=num
binary=""
while t>=1:
    if t==1:
        binary+='1'
    elif t%2==0:
        binary+='0'
    else:
        binary+='1'
    n+=1
    t//=2
binary1=""
for i in binary:
    binary1=i+binary1
print("the binary number for",num,"is",binary1)


    

    
    