from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):        pass
    @abstractmethod
    def perimeter(self):   pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Square(Shape):
    def __init__ (self,side):
        self.side=side


    def area(self):
        return self.side**2
    

    def perimeter(self):
        return self.side+self.side+self.side+self.side

# Example usage
if __name__ == "__main__":
    rect = Rectangle(4, 5)
    print(f"Rectangle area: {rect.area()}")
    print(f"Rectangle perimeter: {rect.perimeter()}")
    circle = Circle(3)
    print(f"Circle area: {circle.area()}")
    print(f"Circle perimeter: {circle.perimeter()}")
    square = Square(4)
    print(f"Square area: {square.area()}")
    print(f"Square perimeter: {square.perimeter()}")