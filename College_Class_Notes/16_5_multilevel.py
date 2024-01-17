# multilevel inheritance

"""It contains a superclass Shape and subclass Rectangle (inheriting from Shape) and 
Square (inheriting from Rectangle)"""
 
class Shape:
    """The superclass Shape with a color"""
    def __init__(self, color = 'red'):
        """Initializer"""
        self.color = color
 
class Rectangle(Shape):
    """The Rectangle class: a subclass of Shape with a length and width"""
    def __init__(self, length = 1.0, width = 1.0, color = 'red'):
        """Initializer"""
        super().__init__(color)
        self.length = length
        self.width = width
 
    def get_area(self):
        return self.length * self.width
 
class Square(Rectangle):
    """The Square class: a subclass of Rectangle having the same length and width"""
    def __init__(self, side = 1.0, color = 'red'):
        """Initializer"""
        super().__init__(side, side, color)
 

# For Testing
if __name__ == '__main__':
    s1 = Shape('orange')
    print(s1.color)          # orange
     
    r1 = Rectangle(1.2, 3.4, 'orange')
    print(r1.get_area())     # 4.08
    print(r1.color)          # orange
    print(r1.length)         # 1.2
    print(r1.width)          # 3.4
     
    sq1 = Square(5.6, 'orange')
    print(sq1.get_area())    # 31.359999999999996
    print(sq1.color)         # orange
    print(sq1.length)        # 5.6
    print(sq1.width)         # 5.6