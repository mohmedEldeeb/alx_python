"""
    This module to creates a smple class rectangle
"""
from models.base import Base

class Rectangle(Base):
    """
    class inherits frombase
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate values"""
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        super().__init__(id)


    @property
    def height(self):
        """
            mathed getter to get private width
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            mathed getter to get private width
        """
        self.toValidation('height', value)
        self.__height = value
    @property
    def width(self):
        """
            mathed getter to get private width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            mathed getter to get private width
        """
        self.toValidation('width', value)
        self.__width = value


    @property
    def y(self):
        """
            mathed getter to get private width
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            mathed getter to get private width
        """
        self.toValidation('y', value)
        self.__y = value
    
    @property
    def x(self):
        """
            mathed getter to get private width
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            mathed getter to get private width
        """
        self.toValidation('x', value)
        self.__x = value

    @staticmethod
    def toValidation(name, value):
        """
            to validation values of height and weight and x and y
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and (name == 'x' or name == 'y'):
            raise ValueError("{} must be >= 0".format(name))
        if value <= 0 and name != 'x' and name != 'y':
            raise ValueError("{} must be > 0".format(name))
        