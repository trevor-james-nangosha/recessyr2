"""
# # Basic Operators and Expressions(Input and Output Operators)
#
# Arthemetic operators
# Addition +
# Subtraction -
# Multiplication *
# Divison /
# Modulus %
# Divide // dont return the reminder
# Exponentiation **
#
# Comparison Operators
# Equal to ==
# Not Equal to !==
# Greater than >
# Less than <
# Greater than or equal to >=
# Less than or equal to <=
#
# Logical Operators
# Logical AND 'and'
# Logical OR  'or'
# Logical NOT 'not
#
# Assignment Operators
# Assign value: '='
# Add Value: '+'
# Add and assign value: '+='
# Sub and assign value: '-=
# Multiply and assign value: '*='
# Divide and assign value: '%='
# Exponentiate and assign value: '**='
#
# Membersip Operators
# In: 'in' Checks if a value exists in a sequence
# Not in:  'not in': checks if valube dont exist in sequence
#
# Identify Operator
# Is: is Checks if 2 values are the same
# Is Not: 'is not' checks if 2 values are not the same
# """
#
# # Examples of Arthemetic operators
# # Addition +
# x = 50+45
# print(x)
# # Subtraction -
# y = 50-45
# print(y)
# # Multiplication *
# u = 50*45
# print(u)
# # Divison /
# i = 50/45
# print(i)
# # Modulus %
# o = 50%45
# print(o)
# # Divide // dont return the reminder
# p = 50//45
# print(p)
# # Exponentiation **
# a = 50**45
# print(a)
#
#
# # Examples Comparison Operators
# a = 15
# b = 9
#
# # Greater than >
# if a > b:
#     print("a is greater than b")
#     print(a > b)
#
# # Equal to ==
# if a == b:
#     print("a is equal to b")
#     print(a == b)
# # Not Equal to !==
# if a != b:
#     print("a is not equal to b")
#     print(a != b)
# # Less than <
# if a < b:
#     print("a is less than b")
#     print(a < b)
# else:
#     print("a is less than b")
#     print(a < b)
# # Greater than or equal to >=
# if a >= b:
#     print("a is greater than or equal to  b")
#     print(a >= b)
# # Less than or equal to <=
# if a <= b:
#     print("a is less than or equal to  b")
#     print(a <= b)
# else:
#     print("a is less than or equal to  b")
#     print(a <= b)
#
# print(a == b)
# print(a != b)
#
# # Examples Logical Operators
# t = True
# f = False
# # Logical AND 'and'
# print(t and f)
# # Logical OR  'or'
# print(t or f)
# # Logical NOT 'not
# print(not t)
# print(not f)
#
# #Assignment Operator
# # Compound Assignment opertaors
# d = 5
# # add and assign
# d += 5
# print(d)
#
# # sub and assign
# b = 19
# b -= 5
# print(b)
#
# # multply and assign
# c = 5
# c *= 5
# print(c)
#
# # divide and assign
# n = 5
# n /= 5
# print(n)
#
# # modulus and assign
# e = 9
# e %= 5
# print(e)
#
# # exponention and assign
# g = 2
# g **= 2
# print(g)
#
# # membership assignment operatorsv
# cars = ["jeep", "tesla", " bmw", "rolroyce"]
#
# if "jeep" in cars:
#     print('jeep is around')
#     print('tesla' in cars)
#     print("toyota" in cars)
# if "tenc" in cars:
#     print('jeep is around')

# identity Operators
# k = 9
# l = 9
# # is operator
# print(k is l)
# print(k is not l)
# print(k == l)
# print(k != l)
#
# #list
# x = [ 1,2,3,4,5]
# z = [ 1,2,3,4,5]
# print(x is not z)

# Bitwise Operator
# used to perform operations on individual bits in a binary number
# bitwise AND (&) performs a bitwise operations btn the correponding bits of two integers
# bitwise OR ('|') performs a bitwise OR operation between the correponding bits of 2 integers
# bitwise XOR ('^') performs a bitwise  XOR operation
# bitwise NOT ('') bitwise opeartion that
# bitwise left shift ('<<') left shift operation
# bitwise right shift ('>>')

#example
# a = 10
# b  = 20

#bitwise add operation
# result_and = a & b
# print(result_and)
#
# # bitwise OR
# result_Or = a | b
# print(result_Or)
#
# #bitwise XOR
# result_xor = a ^ b
# print(result_xor)

# Example
# create a simple calculator function(add, sub, multlpy, divide)
"""

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def div(a,b):
    return a / b

def multiply(a,b):
    return a * b

def main(num1, num2, operator):
    print("mic simple cal")
    num1 = float(input("enter number 1"))
    num2 = float(input("enter number 2"))
    operator = input("Enter te operator (+, -, /, *)")

    if operator == '+':
        result = add(num1,num2)
    elif operator == '-':
        result = sub(num1, num2)
    elif operator == '/':
        result = div(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    else:
        print("invalid operator")
        return
    print("the result is", result)


    if __name__ == '__main__':
        main()

#tkinter learn
#assignment1 create a simple calculator program with GUI interface.
"""



# Import Tkinter
import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("trevor Simple Calculator")

# Create the display
display = tk.Entry(window, width=30, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Create number buttons
button_1 = tk.Button(window, text="1", padx=20, pady=10, bg='red', command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, bg='red', command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, bg='red', command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, bg='yellow', command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, bg='yellow', command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, bg='yellow', command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, bg='green', command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, bg='green', command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, bg='green', command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

# Create operator buttons
button_add = tk.Button(window, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=lambda: button_click("/"))

button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)
button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)

# Position the buttons on the grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)

# Start the GUI main loop
window.mainloop()
