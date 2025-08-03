from abc import ABC,abstractmethod
class baseClass(ABC):
    def print(self,x):
        print("passed number :",x)
    @abstractmethod
    def task(self):
        print("this is inside the baseClass")
class testClass(baseClass):
    def task(self):
        print("The function task is hidden")
obj=testClass()
obj.task()
obj.print(902)
