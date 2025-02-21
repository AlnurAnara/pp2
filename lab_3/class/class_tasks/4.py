'''
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
'''
import math 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print (f"the coordinate is ({self.x},{self.y})")
    
    def move(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
        print(f"The new coordinate is: ({self.x}, {self.y})")

    def dist(self,point):
        result = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2  )
        return result
    
point1=Point(1,2)
point2=Point(4,5)

point1.show()
point2.show()
point1.move(9,10)
print(point1.dist(point2))
