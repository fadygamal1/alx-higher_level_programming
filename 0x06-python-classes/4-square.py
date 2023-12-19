#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 3-square.py)

- Private instance attribute: `size`:
- - property def `size(self):` to retrieve it
- - property setter `def size(self, value):` to set it:
- - - `size` must be an integer, otherwise raise a `TypeError` exception
      with the message `size must be an integer`
- - - if `size` is less than `0`, raise a `ValueErro`r exception with the
      message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square
  area
- You are not allowed to import any module
Why?

    Why a getter and setter?

    Reminder: size is a private attribute. We did that to make
    sure we control the type and value. Getter and setter methods
    are not 100% Python, but more OOP. With them, you will be able
    to validate the assignment of a private attribute and also define
    how getting the attribute value will be available from outside -
    by copy? by assignment? etc. Also, adding type/value validation
    in the setter will centralize the logic, since you will do it
    in only one place.
"""


class Square:
    """The Square class"""

    def __init__(self, size=0):
        """Initialising the Square class"""
        self.size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
