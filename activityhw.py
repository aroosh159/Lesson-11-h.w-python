#import necessary packages
from abc import ABC
#create a base class 
class polygon(ABC):
    #abstract method
    #should be implemented by all sub classes
    def move(self):
        pass
    #sub class
class Triangle(polygon):
    def move(self):
        print("I have 3 sides")
class Quadrilateral(polygon):
    def move(self):
        print("I have 4 sides")
class Pentagon(polygon):
    def move(self):
        print("I have 5 sides")
class Hexagon(polygon):
    def move(self):
        print("I have 6 sides")
print("Us four polygons have total 18 sides")
#Driver code
R = Triangle()
R.move
k= Quadrilateral()
k.move
R = Pentagon()
R.move
K = Hexagon()
K.move