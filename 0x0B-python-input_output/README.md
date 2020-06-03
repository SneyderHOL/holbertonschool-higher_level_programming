# Project 0x0B Python - Input/Output

Project using Python, containing severall scripts with Python.

Concepts:

    Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
    How to open a file
    How to write text in a file
    How to read the full content of a file
    How to read a file line by line
    How to move the cursor in a file
    How to make sure a file is closed after using it
    What is and how to use the with statement
    What is JSON
    What is serialization
    What is deserialization
    How to convert a Python data structure to a JSON string
    How to convert a JSON string to a Python data structure


Decribing each script:

0-read_file.py is a function that reads a text file (UTF8) and prints it to stdout.

1-number_of_lines.py is a function that returns the number of lines of a text file.

2-read_lines.py is a function that reads n lines of a text file (UTF8) and print it to stdout.

3-write_file.py is a function that writes a stromg to a text file (UTF8) and returns the number of character written.

4-append_write.py is a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

5-to_json_string.py is a function that returns the JSON representation of an object (string).

6-from_json_string.py is a function that returns an object (Python data structure) represented by a JSON string.

7-save_to_json_file.py is a function that writes an Object to a text file using a JSON representation.

8-load_from_json_file.py is a function that creates an Object from a "JSON file".

9-add_item.py is a script that adds all arguments to a Python list, and then save them to a file.

10-class_to_json.py is a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

11-student.py is a class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)

12-student.py is a class Student that defines a student by (based on 11-student.py):

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):
        If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved

13-student.py is a class Student that defines a student by (based on 12-student.py):

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):
        If attrs is a list of strings, only attributes name contain in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute

14-pascal_triangle.py is a function that returns a list of lists of integers representing the Pascal's triangle of n.

100-append_after.py is a function that inserts a line of text to a file, after each line containing a specific string.

101-stats.py is a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
        Total file size: File size: <total size>
        where is the sum of all previous (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear, don’t print anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order


read_write_heap.py is a script that finds a string in the heap of a running process, and replaces it.
