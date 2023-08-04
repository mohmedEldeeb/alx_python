#!/usr/bin/python3
"""
class to square element
"""

class Square:
    """
    this class to representing a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square class
        """
        self.__size = self.is_int(size)

    def check_int(self, size):
        """
        to check if the number in int
        """
        if isinstance(size, int):
            return (self.is_negative(size))
        else:
            raise TypeError("size must be an integer")

    def check_negative(self, size):
        """
        to check the number is negatev
        """
        if size >= 0:
            return (size)
        else:
            raise ValueError("size must be >= 0")
