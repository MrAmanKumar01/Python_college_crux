"""
circle.py: The circle module, which defines a Circle class.
"""
from math import pi
 
class Circle:    
    """A Circle instance models a circle with a radius"""
    
    def __init__(self, radius = 1.0):
        """Initializer with default radius of 1.0"""
        self.radius = radius  # Create an instance variable radius
 
    def get_area(self):
        """Return the area of this Circle instance"""
        return pi * self.radius * self.radius
 
# For Testing under Python interpreter
# If this module is run under Python interpreter, __name__ is '__main__'.
# If this module is imported into another module, __name__ is 'circle' (the module name).
if __name__ == '__main__':
    c1 = Circle(5.1)      # Construct an instance
    print(c1.get_area())  # 81.71282491987051
    print(c1.radius)      # 5.1
        
    c2 = Circle()         # Default radius
    print(c2.get_area())  # Invoke member method
 
    c2.color = 'red'  # Create a new attribute for this instance via assignment
    print(c2.color)
    # print(c1.color)  # Error - c1 has no attribute color
 
    # Test doc-strings
    print(__doc__)                  # This module
    print(Circle.__doc__)           # Circle class
    print(Circle.get_area.__doc__)  # get_area() method
 
    print(isinstance(c1, Circle)) # True
    print(isinstance(c2, Circle)) # True
    print(isinstance(c1, str))    # False


