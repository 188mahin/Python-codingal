add1=[1,2,3]
add2=[5,7,6]
add3=map(lambda x,y:x+y,add1,add2)
print(list(add3))
#square
sq1=[4,5,8,10]
sq2=list(map(lambda n:n*n,sq1))
print(sq2)