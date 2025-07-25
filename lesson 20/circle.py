class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self,radius):
        return 3.14*radius**2
    def perimeter(self,radius):
        return 2*3.14*radius
c=circle(9)
print("the radius of the circle is",c.radius )
print(" the area of the circle is",circle(9).area(9))
print(" the perimeter of the circle is",circle(9).perimeter(9))


    