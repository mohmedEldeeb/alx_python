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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

