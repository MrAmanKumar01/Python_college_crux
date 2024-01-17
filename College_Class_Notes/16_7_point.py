# Operator Overloading
# can overload '+', '-', '*', '/', '//' and '%' by overriding member methods 
# __add__(), __sub__(), __mul__(), __truediv__(), __floordiv__() and __mod__(), respectively
"""
point.py: The point module, which defines the Point class
"""
 
class Point:    
    """A Point instance models a 2D point with x and y coordinates"""
 
    def __init__(self, x = 0, y = 0):
        """Initializer, which creates the instance variables x and y with default of (0, 0)"""
        self.x = x
        self.y = y
 
    def __str__(self):
        """Return a descriptive string for this instance"""
        return f'({self.x}, {self.y})'
 
    def __repr__(self):
        """Return a command string to re-create this instance"""
        return f'Point(x={self.x}, y={self.y})'
 
    def __add__(self, right):
        """Override the '+' operator: create and return a new instance"""
        p = Point(self.x + right.x, self.y + right.y)
        return p
 
    def __mul__(self, factor):
        """Override the '*' operator: modify and return this instance"""
        self.x *= factor
        self.y *= factor
        return self
 
# Test
if __name__ == '__main__':
    p1 = Point()
    print(p1)      # (0, 0)
    p1.x = 5
    p1.y = 6
    print(p1)      # (5, 6)
    p2 = Point(3, 4)
    print(p2)      # (3, 4)
    print(p1 + p2) # (8, 10) Same as p1.__add__(p2)
    print(p1)      # (5, 6) No change
    print(p2 * 3)  # (9, 12) Same as p1.__mul__(p2)
    print(p2)      # (9, 12) Changed