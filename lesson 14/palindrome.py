def palindrome(n):
    e=len(n)-1
    s=0
    while s<e:
        if n[s]!=n[e]:
            return False
        s+=1
        e-=1
    return True
n=(7,8,9,0,7)
if palindrome(n):
    print("the tuple n is a palindrome")
else:
    print("the tuple n is not a palindrome")
