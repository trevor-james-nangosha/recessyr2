"""
Advanced topics in Python
Summary
Regular expressoion
Generators and iterators
Decorators
context managers
multithreading and multiprocessing
"""

"""
Regular expession
\d: matches any digit (0-9)
\w: matches any alpanumeric characters
\s: matces any whitespace charater
"""
# matching and searching
# regex re.match(), re.search(), re.findall()
# example 1 Demostracting regex | match first word, match group word, match all numbers
import re

# pattern = "Jf"
# text = "Hello, my name Hello  is Jeff Geoff. I am a programmer wit 15 years of experience"
# matchs = re.search(pattern,text)
# print(matchs)
# # match first words
# match = re.search(r"\w+",text)
# if match:
#     print(match.group())
#
# matches = re.findall(r"\d+",text)
# print(matches)


# valid email format
# def validate_email(email):
#     pattern = r'^[\w\.\-]+@[\w\.-]+\.\w+$'
#     if re.match(pattern,email):
#         return True
#     else:
#         return False
# # Example of using email
# email1 = "mic.mike90@gmail.com"
# email2 = "mic.mike90@gmailcom"
#
# print(validate_email(email1))
# print(validate_email(email2))

"""
Generators and iterators
'yield' generator
'__iter__' iterators
"""


# example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# return the factorial of a number
# print the factorial of a number from 1 - 10

for i in range(1, 10):
    print(factorial(i))



# example
def factorial(n):
    if n == 0:
        yield 1
    else:
        fac = 1
        for i in range(1, n-1):
            fac *= i
            yield fac

# return the factorial of a number
# print the factorial of a number from 1 - 10

for i in range(1, 10):
    print(*factorial(i))


# example
# generate a function that yeilds the square numbers from 1 to 10
def square():
    for i in range(1, 10):
        yield  i ** 2

# create an iterator object that yields square numbers from 1 -1-0
square_iterator =square()

# print fitrst 5 squares of numbers of numbers 1 to 10
for i in range(5):
    print(next(square_iterator))

# Decorators(@my_decorator)
# allowsyou to modify the behaviour of functions or classes without directly changing the source code
def my_decorator(func):
    def inner():
        print("this is the decorator")
        func()
    return inner()

@my_decorator
def outer_decorator():
 print("this is the outer decorator")

outer_decorator()

