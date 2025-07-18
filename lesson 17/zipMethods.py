s1={1,3,5,8,9,26}
s2={'a','c','e','h','i','z'}
s3=list(zip(sorted(s1),sorted(s2)))
print(s3)
l1=[10,20,30,40]
l2=[100,200,300,400]
for x,y in zip(l1,l2[::-1]):
    print(x, y)
stocks=['Reliance','TCS','Infosys']
prices=[2433,1425,1902]
d1={stocks:prices for stocks,prices in zip(stocks,prices)}
print(d1)



