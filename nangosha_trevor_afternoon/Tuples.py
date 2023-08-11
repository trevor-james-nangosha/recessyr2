# Used to store items in a single variables
# Tuples are ordered and unchangeable

phones = ("samsung", "iphones", "tecno")
print(phones)

# Allow for duplicate values
phones = ("samsung", "iphones", "tecno", "samsung", "tenco")
print(phones)

# Activity1 {Use the len() with tuples }
y = len(phones)
print(y)

# Tuple showing different datatypes
tupl = ("rice", "beans")
tuples = (2,3,4,)
print(type(tuples))

#Activity2 {Accessing Tuples, indexing, ranges }
t = phones[1]
w = phones[0:]
print(t)
print(w)

#adding an item
z = list(phones)
z.append("infinix")
print(z)

phones = tuple(z)
print(phones)

#Adding two tuples
laptops = ("dell", "hp", "acer")
laptop= ("samsung",)
laptops +=laptop
new_desktop = laptops + laptop
print(new_desktop)

#for loop in tuples
for t in new_desktop:
    print(t)
    
print(laptops)