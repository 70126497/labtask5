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