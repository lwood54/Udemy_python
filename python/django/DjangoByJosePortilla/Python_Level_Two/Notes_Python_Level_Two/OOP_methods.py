class Circle():

    pi = 3.14

    def __init__(self,radius=1): #the 1 is a default radius value
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius*self.radius

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_radius(876)
print(myc.area())
