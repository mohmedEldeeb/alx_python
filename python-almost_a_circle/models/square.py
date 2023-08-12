"""
    this is semple class implement from  anather class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class named is  square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ 
            to inatialze instantiate class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            mothed that returns a string
        """
        x = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        z = "{}/{} - {}".format(self.x, self.y, self.width)
        return x + z

    @property
    def size(self):
        """
            mathed getter to get private width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method
        """
        self.width = value
        self.height = value