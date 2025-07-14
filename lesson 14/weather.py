weather=(1,1,0,1,0,0,0,0)
rainy=0
sunny=0
for i in range(0,8):
    if weather[i]==0:
        rainy+=1
    else:
        sunny+=1
if sunny>rainy:
    print("good weather")
elif sunny==rainy:
    print("weather is balanced")
else:
    print("bad weather")
