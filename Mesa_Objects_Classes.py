import math
# Define a class

class Circle:
    #  find the area and perimeter of a circle

    def __init__(self, radius):
        self.radius = radius


    def calculatePerimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of the circle is: {perimeter: .2F}")
        return perimeter

    def calculateArea(self):
        area = math.pi * (self.radius ** 2)
        print(f"The area of a circle is: {area: .2f}")
        return area

# Prompt the user to input radius of a circle
input_radius = float(input("Enter the radius of a circle: "))

circle = Circle(input_radius)
perimeter_result = circle.calculatePerimeter()
area_result = circle.calculateArea()


