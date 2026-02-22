def isevenorodd(n):
    if n^1==n+1:
        return True
    else:
        return False
n=int(input("enter a number"))
if isevenorodd(n):
    print("number is even")
else:
    print("number is odd")
