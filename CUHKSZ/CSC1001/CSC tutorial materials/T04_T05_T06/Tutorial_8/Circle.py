from math import pi

class Circle:
    def __init__(self,radius=1):
        self.radius=radius

    def getPerimeter(self):
        return 2*self.radius*pi

    def getArea(self):
        return self.radius*self.radius*pi

    def setRadius(self,radius):
        self.radius=radius







    
