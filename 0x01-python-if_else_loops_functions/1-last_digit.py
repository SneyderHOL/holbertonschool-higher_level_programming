#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (number * -1) % 10
    last_digit = last_digit * -1
else:
    last_digit = number % 10
if last_digit > 5:
    print('Last digit of ' + number.__str__() + ' is ' + last_digit.__str__() + ' and is greater that 5')
elif last_digit == 0:
    print('Last digit of ' + number.__str__() + ' is ' + last_digit.__str__() + ' and is 0')
else:
    print('Last digit of ' + number.__str__() + ' is ' + last_digit.__str__() + ' and is less than 6 and not 0')
