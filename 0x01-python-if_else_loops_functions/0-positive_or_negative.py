#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number.__str__() + ' is positive')
elif number == 0:
    print(number.__str__() + ' is zero')
else:
    print(number.__str__() + ' is negative')
