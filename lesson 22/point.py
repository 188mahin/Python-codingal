class point:
    def __init__(self,x=38,y=50):
        self.x=x
        self.y=y
    def __str__(self):
        return f'({self.x},{self.y})'
p1=point()
print(p1)