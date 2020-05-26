# Project 0x09 Python - Everything is object

Project about Python, containing severall txt files with answer to each task of the project, and some scripts with Python.

Concepts:

    Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
    What is an object
    What is the difference between a class and an object or instance
    What is the difference between immutable object and mutable object
    What is a reference
    What is an assignment
    What is an alias
    How to know if two variables are identical
    How to know if two variables are linked to the same object
    How to display the variable identifier (which is the memory address in the CPython implementation)
    What is mutable and immutable
    What are the built-in mutable types
    What are the built-in immutable types
    How does Python pass variables to functions


Describing each file:

0-answer.txt - What function would you use to print the type of an object?
Write the name of the function in the file, without ().

1-answer.txt - How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without ().

2-answer.txt - In the following code, do a and b point to the same object? Answer with Yes or No.
    >>> a = 89
    >>> b = 100

3-answer.txt - In the following code, do a and b point to the same object? Answer with Yes or No.
    >>> a = 89
    >>> b = 89

4-answer.txt - In the following code, do a and b point to the same object? Answer with Yes or No.
    >>> a = 89
    >>> b = a

5-answer.txt - In the following code, do a and b point to the same object? Answer with Yes or No.
    >>> a = 89
    >>> b = a + 1

6-answer.txt - What do these 3 lines print?
    >>> s1 = "Holberton"
    >>> s2 = s1
    >>> print(s1 == s2)

7-answer.txt - What do these 3 lines print?
    >>> s1 = "Holberton"
    >>> s2 = s1
    >>> print(s1 is s2)

8-answer.txt - What do these 3 lines print?
    >>> s1 = "Holberton"
    >>> s2 = "Holberton"
    >>> print(s1 == s2)

9-answer.txt - What do these 3 lines print?
    >>> s1 = "Holberton"
    >>> s2 = "Holberton"
    >>> print(s1 is s2)

10-answer.txt - What do these 3 lines print?
    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3] 
    >>> print(l1 == l2)

11-answer.txt - What do these 3 lines print?
    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3] 
    >>> print(l1 is l2)

12-answer.txt - What do these 3 lines print?
    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 == l2)

13-answer.txt - What do these 3 lines print?
    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 is l2)

14-answer.txt - What does this script print?
    l1 = [1, 2, 3]
    l2 = l1
    l1.append(4)
    print(l2)

15-answer.txt - What does this script print?
    l1 = [1, 2, 3]
    l2 = l1
    l1 = l1 +[4]
    print(l2)

16-answer.txt - What does this script print?
    def increment(n):
    	n += 1
	
    a = 1
    increment(a)
    print(a)

17-answer.txt - What does this script print?
    def increment(n):
    	n.append(4)
	
    l = [1, 2, 3]
    increment(l)
    print(l)

18-answer.txt - What does this script print?
    def assign_value(n, v):
    	n = v
	
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    assign_value(l1, l2)
    print(l1)

19-copy_list.py is a function that returns a copy of a list.

20-answer.txt - Is a a tuple? Answer with Yes or No.
    a = ()

21-answer.txt - Is a a tuple? Answer with Yes or No.
    a = (1, 2)

22-answer.txt - Is a a tuple? Answer with Yes or No.
    a = (1)

23-answer.txt - Is a a tuple? Answer with Yes or No.
    a = (1, )

24-answer.txt - What does this script print?
    a = (1)
    b = (1)
    a is b

25-answer.txt - What does this script print?
    a = (1)
    b = (1)
    a is b

26-answer.txt - What does this script print?
    a = (1)
    b = (1)
    a is b

27-answer.txt - Will the last line of this script print 139926795932424? Answer with Yes or No.
    >>> id(a)
    139926795932424
    >>> a
    [1, 2, 3, 4]
    >>> a = a + [5]
    >>> id(a)

28-answer.txt - Will the last line of this script print 139926795932424? Answer with Yes or No.
    >>> a
    [1, 2, 3]
    >>> id (a)
    139926795932424
    >>> a += [4]
    >>> id(a)


106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt

How many string objects are created by the execution of the first line of the script? (106-line1.txt)
How many string objects are created by the execution of the second line of the script (106-line2.txt)
After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
How many string objects are created by the execution of the last line of the script (106-line5.txt)

    cat string.py 
    a = "HBTN"
    b = "HBTN"
    del a
    del b
    c = "HBTN"


100-magic_string.py is a function that returns a string "Holberton" n times the number of the iteration.

101-locked_class.py is a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

103-line1.txt, 103-line2.txt

How many int objects are created by the execution of the first line of the script? (103-line1.txt)
How many int objects are created by the execution of the second line of the script (103-line2.txt)

    cat int.py 
    a = 1
    b = 1


104-line1.txt, 104-line2.txt, 104-line3.txt, 104-line4.txt, 104-line5.txt

How many int objects are created by the execution of the first line of the script? (104-line1.txt)
How many int objects are created by the execution of the second line of the script (104-line2.txt)
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
How many int objects are created by the execution of the last line of the script (104-line5.txt)

    cat int.py 
    a = 1024
    b = 1024
    del a
    del b
    c = 1024


105-line1.txt

Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
Why? (optional blog post :))

cat int.py 
print("I")
print("Love")
print("Python")
