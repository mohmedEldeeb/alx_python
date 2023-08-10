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
