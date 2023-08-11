"""
Exception Handling Example
ZeroDivisionError
# TypeError
# ValueError
# NameError
# FileNotFoundError
# IndexError
# KeyError
# AttributeError
# ImportError
# IOError
"""
# Division by zero: ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# Index out of range: IndexError
try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError:
    print("Error: Index out of range!")

# File not found: FileNotFoundError
try:
    file = open("nonexistent_file.txt", "r")
except FileNotFoundError:
    print("Error: File not found!")

# Type conversion error: ValueError
try:
    value = int("abc")
except ValueError:
    print("Error: Invalid value for conversion!")

"""
 Custom exception
 This is done for when the programmer wants to customize an expection
 One must inheritant the Exception class  to create a custom expection
"""


class MyExceptionError(Exception):
    pass


try:
    raise MyExceptionError("My Error exception raised!")
except MyExceptionError as e:
    print("Error:", str(e))

"""
Multiple exceptions
This is done when there are many error tat can occur on one function or method
Hence having many exceptions to catch all the errors that may occur
"""
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


"""
File Handling
"""

"""
Create a file
"""
file = open("sample.txt", "w") # this creates the file its not there
file.write("My Name is nangosha trevor")
file.close()

"""
Read the file
"""
file = open("sample.txt", "r")
in_file = file.read()
print("Content:", in_file)
file.close()

"""
Append to the file
"""
file = open("sample.txt", "a")
file.write("\nI love my name.")
file.close()

"""
Read the file line by line
"""
file = open("sample.txt", "r")
by_lines = file.readlines()
print("Lines:")
for line in by_lines:
    print(line.strip())  # Strip newlines and whitespaces
file.close()

"""
 Check if a file exists
"""
import os
if os.path.exists("sample.txt"):
    print("File exists.")
else:
    print("File does not exist.")

"""
Rename the file
"""
os.rename("sample.txt", "new_sample.txt")

"""
Delete the file
"""
os.remove("new_sample.txt")

"""
Check if the file exists (after deletion)
"""
if os.path.exists("new_sample.txt"):
    print("File exists.")
else:
    print("File does not exist.")
