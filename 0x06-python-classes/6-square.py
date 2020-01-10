#!/usr/bin/python3
"""Square that defines a square by
       size = no type value
"""


class Square:
    """Square that defines a square by
       size = no type value
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
            self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
        

    def my_print(self):
        if self.__size == 0:
            print("\n", end='')
        else:
            for i in range(self.__size):
                    print('#' * self.__size)

    	
