def factorial(x):
    '''this is a recursive function for finding the factorial of a number'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
n=int(input("enter a number:"))
print(factorial.__doc__)
print(f"the factorial of {n} is {factorial(n)}")

