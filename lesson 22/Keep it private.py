class myClass:
    __privateVar=47
    def __privMeth(self):
        print("I am private")
    def hello(self):
        print("my private number is",myClass.__privateVar)
obj=myClass()
obj.hello()
obj.__privMeth()