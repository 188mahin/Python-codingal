class B:
    def __init__(self,a):
        self.a=a
    def __eq__(self, other):
        if self.a==other.a:
            return "Both are equal"
        else:
            return "not equal"
    def __lt__(self, other):
        if self.a<other.a:
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
ob1=B(4)
ob2=B(9)
print(ob1<ob2)
print(ob1==ob2)