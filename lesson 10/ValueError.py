try:
    n=int(input("enter a number:"))
    print(f"the number is {n}")
except ValueError as ex:
    print(f"exception: {ex}")