# Functions
# Group blocks of code
# There is need for code that is clean reusable and maintainable
# synatx for a function is def
# def function_name():
#
# def afternoon(f_name, l_name):
#     print("It the afternoon class")
#     print(f_name)
#     print("Attendences close to 100")
#     print(l_name)
#     print(f"Hi {f_name} {l_name}")
#
#
# # calling a function
# afternoon("livingstone", "Jon")


# arguments and parameters
# arguments are specified after the function name
# paraments are the

# Modules
# can a file comtaining any python files
# simple calc
# def add(a, b):
#     return (a + b)
#
#
# def product(a, b):
#     return (a * b)
#
#
# # import nangosha_trevor_day4_afternoon
# # print(nangosha_trevor_day4_afternoon.product(3, 3))
#
# #importing square roots and fatorial from the math module
# from math import sqrt, factorial
# # import math as mt
#
# from math import *
# print(sqrt(16))
# print(factorial(4))
#
# # input and output in python
# # input("prompt")
#
# name = input("Enter your name: ")
# print("your name is ", name)
#
# # example2
# number1 = int(input("enter the value: "))
# Product = number1*2
# print(Product)

# example3 multple imputs in python
# s, r, w = map(int, input("Enter the values: ").split())
# print("the values are : ", end="")
# print(s, r, w)

# how to capture inputs from a tuple
w =  (2,4,5,6,7)
print("cureent tuple")
print(w)

# e = list(w)
# e.append(int(input("enter new value: ")))
# w = tuple(e)
# print("updated tuple")
# print(w)
# print(type(w))

# set
mylist = list(map(int, input("enter the values: ").split()))
myset = set(map(int, input("enter te set values: ").split()))

print(mylist)
print(type(mylist))
print(myset)
print(type(myset))