from math import pi

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

    
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name, width, height)
        
    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name, None, None)  # Since a circle does not have explicit width and height
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self.radius