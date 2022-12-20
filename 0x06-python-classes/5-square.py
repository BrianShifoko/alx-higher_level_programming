#!/usr/bin/python3
"""
Square Class: Printing a square with #
"""


class Square:
    """ class Square that defines a square """
    def __init__(self, size=0):
        """ Initialize attributes"""
        self.size = size

    @property
    def size(self):
        """ gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size with safe Assignment"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """ prints in stdout the square with the character # """
        if (self.size != 0):
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print('')
        else:
            print('')
