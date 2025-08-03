
"""
#Getter and Setter and more
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width}cm"

    @property
    def height(self):
        return f"{self._height}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width

    @width.deleter
    def width(self):
    del self._width
    print("Width has been deleted")

"""
