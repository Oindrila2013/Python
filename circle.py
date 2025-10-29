class Circle():
    
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def areaCircle(self):
        return self.length * self.width
    
newCircle = Circle(20,30)

print("Dimension of Circle, width = %d , length = %d " %(newCircle.width, newCircle.length))
print("Area of Circle is", newCircle.areaCircle())