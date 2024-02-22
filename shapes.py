class Shape():
    def __init__(self, name, width=None, height=None):
        self._name = name
        if width is not None and height is not None:
            self._width = width
            self._height = height
        else:
            raise ValueError("Both width and height must be provided.")

    @property
    def name(self):
        return self._name

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def calculate_area(self):
        if self._width is not None and self._height is not None:
            return self._width * self._height
        else:
            raise ValueError("Width and height are required to compute area.")

    def calculate_perimeter(self):
        if self._width is not None and self._height is not None:
            return 2 * (self._width + self._height)
        else:
            raise ValueError("Width and height are required to compute perimeter.")
        
        from math import pi

class Shape():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self._width = width
        self._height = height
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
        
    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value

    def calculate_area(self):
        return pi * (self._radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self._radius
    