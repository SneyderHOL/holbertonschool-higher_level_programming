# Project 0x0A Python - Inheritance

Project using Python, containing severall scripts with Python.

Concepts:

    Why Python programming is awesome
    What is a superclass, baseclass or parentclass
    What is a subclass
    How to list all attributes and methods of a class or instance
    When can an instance have new attributes
    How to inherit class from another
    How to define a class with multiple base classes
    What is the default class every class inherit from
    How to override a method or attribute inherited from the base class
    Which attributes or methods are available by heritage to subclasses
    What is the purpose of inheritance
    What are, when and how to use isinstance, issubclass, type and super built-in functions


Decribing each script:

0-lookup.py is a function that returns the list of available attributes and methods of an object.

1-my_list.py is a class called MyList that inherits from list, test/1-my_list.txt doctest for 1-my_list.py file.

2-is_same_class.py is a function that returs True if the object is exactly an instance of the specified class; otherwise False.

3-is_kind_of_class.py is a function that returns True if the object is an instance of, or if the objects is an instance of a class that inherited from, the specified class; otherise False.

4-inherits_from.py is a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

5-base_geometry.py is an empty class called BaseGeometry.

6-base_geometry.py is a class called BaseGeometry (based on 5-base_geometry.py)

    Public instance method: def area(self): that raises an Exception with the message area() is not implemented
    You are not allowed to import any module

7-base_geometry.py is class called BaseGeometry (based on 6-base-geometry.py), test/7-base_geometry.txt doctest for 7-base_geometry.py file.

    Public instance method: def integer_validator(self, name, value): that validates value:

        you can assume name is always a string
    	if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
    	if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0


8-rectangle.py is a class called Rectangle that inherits from BaseGeometry (7-base_geometry.py)

    Instantiation with width and height: def __init__(self, width, height):

        width and height must be private. No getter or setter
    	width and height must be positive integers, validated by integer_validator


9-rectangle.py is a class called Rectangle that inherits from BaseGeometry (7-base_geometry.py), (task based on 8-rectangle.py)

    Instantiation with width and height: def __init__(self, width, height)::
        width and height must be private. No getter or setter
        width and height must be positive integers validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>


10-square.py is a class called Square that inherits from Rectangle (9-rectangle.py):

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented


11- square.py is a class called Square that inherits from Rectangle (9-rectangle.py), (task based on 10-square.py).

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the square description: [Square] <width>/<height>


100-my_int.py is a class called MyInt that inherits from int:

    MyInt is a rebel. MyInt has == and != operators inverted
    You are not allowed to import any module


101-add_attribute.py is a function that adds a new attribute to an object if it's possible:

    Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
    You are not allowed to use try/catch
    You are not allowed to import any module
