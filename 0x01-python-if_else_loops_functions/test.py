#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
num = number[-1]
if int(num) > 5:
    print(f'last digit of {number} is {num} and is greater than 5')
if int(num) < 6 and not int(num) == 0:
    print(f'last digit of {number} is {num} and is less than 6 and not 0')
if int(num) == 0:
    print(f'last digit of {number} is {num} and is 0')
