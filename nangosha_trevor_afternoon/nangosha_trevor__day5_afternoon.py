# # Excception Handling
# """
# ZeroDivisionError
# TypeError
# ValueError
# NameError
# FileNotFoundError
# IndexError
# KeyError
# AttributeError
# ImportError
# IOError
# """
# # try:
# #     a = int(input("Enter Number1: "))
# #     b = int(input("Enter Number2: "))
# #     c =a/b
# #     print("Answer is: ", c)
# #
# # except ZeroDivisionError:
# #     print("Zero Divison Error. Enter Divisor as not Zero")
# #
# # except ValueError:
# #     print(" value Error Enter Integers")
# #
# # except:
# #     print("unknown error")
# #
# # finally:
# #     print(" Executed")
# #
# # phones = ["ph1","ph2","ph3"]
# # try:
# #     print(phones[3])
# # except IndexError:
# #     print("Index Number not in Phones")
#
# # # create your own expection
# # class myError(Exception):
# #     def __init__(self,message):
# #         self.message = message
# #
# #     def __str__(self):
# #         return f"My Error: {self.message}"
# #
# # try:
# #     age = int(input("enter age"))
# #     if age < 0 :
# # except myError:
# #     print("less than zero age")
#
# # file handling
# """
# # modes
# r = read
# w = write
# a = append
# """
# # opening file
# file = open("sample.txt","r")
#
# # reading the contents in the file
# content = file.read()
# print(content)
# file.close() # closing the file
#
# # writing
# file = open("sample.txt", "w")
# file.write("write here")
# print(file)
# file.close()
#
# #appending
# file = open()
# file.write("text")
# file.close()
#
# #delete
# import os
# os.remove("sample.txt")
# print("file deleted")
#
#

# File Handling Example

# Create a file
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

# Read the file
file = open("example.txt", "r")
content = file.read()
print("Content:", content)
file.close()

# Append to the file
file = open("example.txt", "a")
file.write("\nThis is a new line.")
file.close()

# Read the file line by line
file = open("example.txt", "r")
lines = file.readlines()
print("Lines:")
for line in lines:
    print(line.strip())  # Strip newlines and whitespaces
file.close()

# Check if a file exists
import os
if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")

# Rename the file
os.rename("example.txt", "new_example.txt")

# Delete the file
os.remove("new_example.txt")

# Check if the file exists (after deletion)
if os.path.exists("new_example.txt"):
    print("File exists.")
else:
    print("File does not exist.")





# expection
import os

# File Handling Example

try:
    # Create a file
    file = open("example.txt", "w")
    file.write("Hello, World!")
    file.close()

    # Read the file
    file = open("example.txt", "r")
    content = file.read()
    print("Content:", content)
    file.close()

    # Append to the file
    file = open("example.txt", "a")
    file.write("\nThis is a new line.")
    file.close()

    # Read the file line by line
    file = open("example.txt", "r")
    lines = file.readlines()
    print("Lines:")
    for line in lines:
        print(line.strip())  # Strip newlines and whitespaces
    file.close()

    # Check if a file exists
    if os.path.exists("example.txt"):
        print("File exists.")
    else:
        print("File does not exist.")

    # Rename the file
    os.rename("example.txt", "new_example.txt")

    # Delete the file
    os.remove("new_example.txt")

    # Check if the file exists (after deletion)
    if os.path.exists("new_example.txt"):
        print("File exists.")
    else:
        print("File does not exist.")

except Exception as e:
    print("An error occurred:", str(e))


# Exception Handling Example

# Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# Index out of range
try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError:
    print("Error: Index out of range!")

# File not found
try:
    file = open("nonexistent_file.txt", "r")
except FileNotFoundError:
    print("Error: File not found!")

# Type conversion error
try:
    value = int("abc")
except ValueError:
    print("Error: Invalid value for conversion!")

# Custom exception
class MyException(Exception):
    pass

try:
    raise MyException("Custom exception raised!")
except MyException as e:
    print("Error:", str(e))

# Multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Error: Invalid input!")
except ZeroDivisionError:
    print("Error: Division by zero!")
except Exception as e:
    print("An unexpected error occurred:", str(e))
else:
    print("No exceptions occurred.")
finally:
    print("Execution completed.")
