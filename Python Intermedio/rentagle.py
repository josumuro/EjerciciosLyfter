class Rentangle:
    def __init__(self,width,heigth):
        if width<=0 or heigth<=0:
            raise ValueError("Width and height must be positive numbers.")
        self.width=width
        self.heigth=heigth
    def get_area(self):
        return self.width*self.heigth
    def get_perimeter(self):
        return 2*(self.width+self.heigth)
    
rentangle=Rentangle(5,10)
print("The area of the rectangle is:", rentangle.get_area())
print("The perimeter of the rectangle is:", rentangle.get_perimeter())

