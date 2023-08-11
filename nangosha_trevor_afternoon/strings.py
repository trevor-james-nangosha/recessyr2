#works
#use len() function to detemine the length of your string
#give an example of using a for loop in a string
#give example of slicing in strings


"""
STRINGS.
Strings are immutable
"""
names = "Clark Kent"    # String creation

# Multi line strings
saf = """This 
is a multi line 
string"""
print(saf)

# Accessing characters in a string:
print(names[0])
print(names[6])
print(names[-1])

# String concatenation
string1 = "My"
string2 = "food"
concatenated_string = string1 + " " + string2
print(concatenated_string)

# Activity1 : Use the len() function
# String length
print(len(names))  # returns the number of characters (including whitespace and special characters) in the string.

# Activity2 : Use a for loop in a string
for name in names:
    print(name)

# Activity3 : Give an example of slicing in strings
# String slicing
print(names[6:10])
print(names[:5])
print(names[6:])

# String methods
print(names.upper())
print(names.lower())
print(names.startswith("A"))
print(names.startswith("C")) # returns true or false
print(names.split(" "))

# String formatting
anime = "Attack On Titan"
ratings = 10
formatted_string = "{} has a rating of {}.".format(anime, ratings)
print(formatted_string)

# this example shows you that variables must first be defined
# print('{} is my favorite sport'.format(element))      # will return a NameError
element = 'Football'

# STRING MANIPULATION.
# .title() ..  title method capitalizes all first letters in each word of a string.
character = "eren yeager"
print(character.title())

# .replace()  .. takes in two values, one that it searches for and the other that it replaces the searched value with
# replacing an exclamation point with a period
words = "Hello there!"
print(words.replace("!", "."))

# .find()  ..  find method will search for any string we ask it to.
greet = "A good afternoon to you."
index = greet.find("o")
print(index)

index = greet.find("you")
print(index)

index = greet.find("Python")
print(index)   # Output: -1

# .strip() can be used to get rid of a certain character on the left and right side of a string. By default, it will remove spaces.
require = "   Unknown to all mankind   "
stripped_string = require.strip()
print(stripped_string)

req = "...Known to a few people..."
stripped_string = req.strip(".")
print(stripped_string)

left_stripped_string = req.lstrip(".")   # using lstrip()
print(left_stripped_string)

right_stripped_string = req.rstrip(".")  # using rstrip()
print(right_stripped_string)

stri = "After noon"
print(stri.replace(" ", ""))
