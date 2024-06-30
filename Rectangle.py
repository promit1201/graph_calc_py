class Rectangle:
    def set_dimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)
#self is a keyword for recalling the function, its a default parameter that doesn't need to be passed
rect1 = Rectangle()
rect1.set_dimensions(10,20)
print(rect1.area())
print(rect1.perimeter())