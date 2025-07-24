class destruct:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("destructor called")
def create():
    print("making object...")
    obj=destruct()
    print("function ends...")
    return obj
print("calling create function...")
obj=create()
print("program ends...")