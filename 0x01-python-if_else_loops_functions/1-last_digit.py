#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = abs(number) % 10
if number < 0:
    ldigit = -ldigit
print(f"Last digit of {number:d} is {ldigit:d} and is ", end="")
if ldigit == 0:
    print("0")
elif ldigit > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
