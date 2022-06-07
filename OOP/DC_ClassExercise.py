import math as math
# two attributes, x and y - the coordinates of the point on the plane;

# A constructor that accepts two arguments, x and y, that initialize the corresponding attributes. These arguments should have default value of 0.0;
# A method distance_to_origin() that returns the distance from the point to the origin. The formula for that is .
# A method reflect(), that reflects the point with respect to the x- or y-axis:
# accepts one argument axis,
# if axis="x" , it sets the y (not a typo!) attribute to the negative value of the y attribute,
# if axis="y", it sets the x attribute to the negative value of the x attribute,
# for any other value of axis, prints an error message.

# Write the class Point as outlined in the instructions
import math as math


# Write the class Point as outlined in the instructions
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def reflect(self, axis):
        if axis.lower() == "x":
            self.y = -self.y

        elif axis.lower() == "y":
            self.x = -self.x

        else:
            print("You have entered an illegal value for axis")


pt = Point(x=3.0)
pt.reflect("1")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())