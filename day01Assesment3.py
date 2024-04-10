class Circle:

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return f"This circle Area is(22/7*radius*radius):{22/7*self.radius*self.radius}"

    def getCircumference(self):
        return f"This circle Circumference is(2*22/7*radius):{2*3.14*self.radius}"

n = float(input("enter  the redis :: "))
circle1 = Circle(n)   # object creation

area = circle1.getArea()
circumference = circle1.getCircumference()

print("area ::", area)

print("*=====================*====================*==================*==============*")

print("circumference ::", circumference)