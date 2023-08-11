# Checking Datatypes
w = 40
print(type(w))

z = "Hello World"
print(type(z))

y = 1j
print(type(y))

z = (1, 2, 3)
print(type(z))

t = {1, 2, 3}
print(type(t))

# LISTS
# Used to store items in a single variable
#Lists are ordered, changeable, Allow duplicate values

Afternoon = ["White", "Silver", "Brown"]
print(Afternoon)

After = ["White", "Silver", "Brown", "White", "Silver", "Brown", "Blue"]
print(After)

#length of list
print(len(After))

#Type
print(type(After))

#Acess to list
print(After[2])
print(After[6])

#List Operations
my_list = [1,2,3,4]

new_list = my_list.append(5)
print(new_list)

n_list = my_list.remove(3)
print(n_list)

print(my_list[-2])
print(my_list[-3])

mixed_list = [1, "name", True]

nested = [[1,2,3], [4,5,6], [7,8,9]]

#range
print(After[2:4])
print(After[:1])
print(After[5:])

#Insert
After.insert(0 ,"Yellow")
print(After)

#Append
After.append("Yellow")
print(After)

#Remove
After.remove("Blue")
print(After)

#Remove by Index
After.pop(6)
print(After)