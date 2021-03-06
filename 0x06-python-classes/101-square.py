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

        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise ValueError('position must be a tuple of 2 positive integers')
        elif type(position[0]) and type(position[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        else:
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
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise ValueError('position must be a tuple of 2 positive integers')
        elif type(value[0]) and type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("\n", end='')
        else:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.position[0], end='')
                print('#' * self.__size)

    def __str__(self):
        if self.__size == 0:
            return ''
        else:
            a = "\n" * self.__position[1]
            e = (" " * self.__position[0] + '#' * self.__size + "\n")
            i = (" " * self.__position[0] + '#' * self.size)
            return a + e * (self.__size - 1) + i
