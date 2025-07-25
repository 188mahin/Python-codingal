class person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print('id:',self.id,'name:',self.name)
class employee(person):
    def __init__(self,id,name,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,id,name)
a=employee(960089,'John',90000,'intern')
a.display()
