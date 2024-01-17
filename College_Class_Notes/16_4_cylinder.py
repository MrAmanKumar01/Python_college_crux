# override the get_area() method to return the surface area of the cylinder. 
# get_volume() uses the superclass' get_area(), instead of this class.

# super() return a proxy object that delegates method calls to a parent or sibling class. 
# This is useful for accessing inherited methods that have been overridden in a class.
# https://docs.python.org/3/library/functions.html#super

"""cylinder.py: The cylinder module, which defines the Cylinder class"""

from math import pi
from circle import Circle  # Using the Circle class in the circle module

class Cylinder(Circle):
    """The Cylinder class is a subclass of Circle"""
    
    def __init__(self, radius = 1.0, height = 1.0):
        """Initializer"""
        super().__init__(radius)  # Invoke superclass' initializer
        self.height = height
 
    # Override
    def get_area(self):
        """Return the surface area the cylinder"""
        return 2.0 * pi * self.radius * self.height
 
    def get_volume(self):
        """Return the volume of the cylinder"""
        return super().get_area() * self.height  # Use superclass' get_area()
 
# For testing
if __name__ == '__main__':
    cy1 = Cylinder(1.1, 2.2)
    print(cy1.get_area())   # Invoke overridden version
    print(cy1.get_volume()) # Invoke own method
    print(cy1.radius)
    print(cy1.height)
     
    cy2 = Cylinder()        # Default radius and height
    print(cy2.get_area())
    print(cy2.get_volume())
        
