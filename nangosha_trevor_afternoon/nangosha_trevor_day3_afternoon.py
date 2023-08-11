# LISTS
print("Activity 1 LISTS")
#1
print("Activity 1 LISTS")
print("Activity 1 Number 1")
print("Create a list with 5 items (names of people) and write a python program to output the 2nd item")
names = ["mike", "james","john","eren","yeager"]
print(names[1])
print("*****************************************************************************")

#2
print("Activity 1 LISTS")
print("Activity 1 Number 2")
print("Write a python program to change the value of the first item to a new value")
names[1] = "Ackerman"
print(names[1])
print("*****************************************************************************")

#3
print("Activity 1 LISTS")
print("Activity 1 Number 3")
print(" Write a python program to add a sixth item to the list")
names.append("Mikasa")
print(names)
print("*****************************************************************************")

#4
print("Activity 1 LISTS")
print("Activity 1 Number 4")
print(" Write a python program to add “Bathel” as the 3rd item in your list")
names.insert(2,"Bathel")
print(names)
print("*****************************************************************************")

#5
print("Activity 1 LISTS")
print("Activity 1 Number 5")
print(" Write a python program to remove the 4th item from the list")
names.remove(names[3])
print(names)
print("*****************************************************************************")

#6
print("Activity 1 LISTS")
print("Activity 1 Number 6")
print("Use negative indexing to print the last item in your list")
print(names[-1])
print("*****************************************************************************")

#7
print("Activity 1 LISTS")
print("Activity 1 Number 7")
print("Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items")
new_name = ["peter", "james","mike", "james","john","eren","yeager"]
print(new_name[3:5])
print("*****************************************************************************")

#8
print("Activity 1 LISTS")
print("Activity 1 Number 8")
print("Write a list of countries and make a copy of it.")
Countries = ["USA", 'Canada', 'Mexico','Uganda']
new_country = Countries.copy()
print(Countries)
print(new_country)
print("*****************************************************************************")

#9
print("Activity 1 LISTS")
print("Activity 1 Number 9")
print("Write a python program to loop through the list of countrie")
for Country in Countries:
    print(Country)
print("*****************************************************************************")


#10
print("Activity 1 LISTS")
print("Activity 1 Number 10")
print("Write a list of animal names and sort them in both descending and ascending order")
animals = ["cats","tiger", "pig","cow","lion"]
animals.sort()

t=animals.sort(reverse=1)
print(t)
print("*****************************************************************************")

#11
print("Activity 1 LISTS")
print("Activity 1 Number 11")
print("sing the list above, write a python program to output only animal names with the letter ‘a’ in them")
for Animal in animals:
    print(Animal)
print("*****************************************************************************")

#12
print("Activity 1 LISTS")
print("Activity 1 Number 12")
print("Write two lists, one containing your first names and the other your second names. Join the two lists.")
f_name = ["nangosha","alice", "jon"]
v = set(f_name)
l_name = ["trevor","mary","snow"]
n = set(l_name)
joined_list = v.union(n)
m = list(joined_list)
print(type(m))
print("*****************************************************************************")

#tuple
print("Activity 2 TUPLES")
#1
print("Activity 2 TUPLES")
print("Activity 2 Number 1")
print(" Consider the tuple below;x = (“samsung”, “iphone”, “tecno”, “redmi”) Write a python program to output your favorite phone brand.")
x = ("samsung","iphone","tenco","redmi")
print(x[2])
print("*****************************************************************************")

#2
print("Activity 2 TUPLES")
print("Activity 2 Number 2")
print("Use negative indexing to print the 2nd last item in your tuple")
print(x[-2])
print("*****************************************************************************")

#3
print("Activity 2 TUPLES")
print("Activity 2 Number 3")
print("Using the phones list above, write a python program to update “iphone” to “itel”")
xl = list(x)
xl[1] = "itel"
x = tuple(xl)
print(x)
print("*****************************************************************************")

#4
print("Activity 2 TUPLES")
print("Activity 2 Number 4")
print("Write a python program to add “Huawei” to your tuple")
xx = list(x)
xx.append("Huawei")
x = tuple(xx)
print(x)
print(type(x))
print("*****************************************************************************")

#5
print("Activity 2 TUPLES")
print("Activity 2 Number 5")
print("Write a python program to loop through the tuple above.")
for phone in x:
    print(phone)
print("*****************************************************************************")

#6
print("Activity 2 TUPLES")
print("Activity 2 Number 6")
print("Write a python program to remove/delete the first item in your tuple.")
my_tuple = (10,20,30,40,50,60)
List = list(my_tuple)
List.pop(0)
Tuple = tuple(List)
print(Tuple)
print("*****************************************************************************")

#7
print("Activity 2 TUPLES")
print("Activity 2 Number 7")
print("Using the tuple() constructor, create a tuple of the cities in Uganda")
uganda_cities = tuple(["kampala","jinja","mengo","Mbarara"])
print(uganda_cities)
print("*****************************************************************************")

#8
print("Activity 2 TUPLES")
print("Activity 2 Number 8")
print("Write a python program to unpack your tuple.")
a,b,c,d = uganda_cities
print(a)
print(b)
print(c)
print(d)
print("*****************************************************************************")

#9
print("Activity 2 TUPLES")
print("Activity 2 Number 9")
print("Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above")
print(uganda_cities[1:4])
print("*****************************************************************************")

#10
print("Activity 2 TUPLES")
print("Activity 2 Number 10")
print("Write two tuples, one containing your first names and the other your second names. Join the two tuples")
first_name = ("john","jane","jake" )
second_name = ("mike", "mic", "snow")
fullname = first_name + second_name
print(fullname)
print("*****************************************************************************")

#11
print("Activity 2 TUPLES")
print("Activity 2 Number 11")
print(". Create a tuple of colors and multiply it by 3")
color = ('red','yellow','blue')
multiply = color*3
print(multiply)
print("*****************************************************************************")

#12
print("Activity 2 TUPLES")
print("Activity 2 Number 12")
print(" Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)")
this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(this_tuple.count(8))
print("*****************************************************************************")

# SETS
print("Activity 3 SETS")
#1
print("Activity 3 SETS")
print("Activity 3 Number 1")
print("Use the set() constructor to create a set of 3 of your favorite beverages")
favorite_beverages = set(["soda","coffee","tea"])
print(favorite_beverages)
print("*****************************************************************************")

#2
print("Activity 3 SETS")
print("Activity 3 Number 2")
print("Use the correct method to add 2 more items to the beverages set.")
favorite_beverages.add("water")
favorite_beverages.add("porriage")
print(favorite_beverages)
print("*****************************************************************************")

#3
print("Activity 3 SETS")
print("Activity 3 Number 3")
print("Given the set below; mySet = {“oven”, “kettle”, “microwave”, “refrigerator”} Check if microwave is present in the set.")
myset = {'oven', 'kettle','mircowave','refrigerator'}
if("mircowave" in myset):
    print("Mircowave is there")
else:
    print("its not there")
print("*****************************************************************************")

#4
print("Activity 3 SETS")
print("Activity 3 Number 4")
print("Write a python program to remove “kettle” from the set above.")
myset.remove("kettle")
print(myset)
print("*****************************************************************************")

#5
print("Activity 3 SETS")
print("Activity 3 Number 5")
print("Write a python program to loop through the set above.")
for item in myset:
    print(item)
print("*****************************************************************************")

#6
print("Activity 3 SETS")
print("Activity 3 Number 6")
print(" Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set")
mylist = {'mike', "two"}
ylisr = [5,8]
i = mylist.union(ylisr)
print(i)
print("*****************************************************************************")

#7
print("Activity 3 SETS")
print("Activity 3 Number 7")
print(" Write two sets, one containing your ages and the other your first names. Join the two sets.")
ages = {24,20,30,50}
f_name = {'jon', 'mic','mike'}
combianed = ages.union(f_name)
print(combianed)
print("*****************************************************************************")

#STRINGS
print("Activity 4 STRINGS")
#1
print("Activity 4 STRINGS")
print("Activity 4 Number 1")
print(" Declare two variables, an integer and a string and use the correct method to concatenate the two variables.")
number = 9
text = "ratings "
joined = str(number) + text
print(joined)
print("*****************************************************************************")

#2
print("Activity 4 STRINGS")
print("Activity 4 Number 2")
print(". Consider the example below;txt = “ Hello, Uganda! ” Output the string without spaces at the beginning, in the middle and at the end.")
txt = " Hello, Uganda! "
strip = txt.strip()
print(strip)
print("*****************************************************************************")

#3
print("Activity 4 STRINGS")
print("Activity 4 Number 3")
print("Write a python program to convert the value of ‘txt’ to uppercase")
texts = " Hello, Uganda! "
upper_case = texts.upper()
print(upper_case)
print("*****************************************************************************")

#4
print("Activity 4 STRINGS")
print("Activity 4 Number 4")
print("Write a python program to replace character ‘U’ with ‘V’ in the string above.")
replace = texts.replace('U','V')
print(replace)
print("*****************************************************************************")

#5
print("Activity 4 STRINGS")
print("Activity 4 Number 5")
print(" Using the code below, write a python program to return a range of characters in the 2nd,3rd and 4th position.y = “I am proudly Ugandan”")
y = "i like being alone"
range = y[1:3]
print(range)
print("*****************************************************************************")

#6
print("Activity 4 STRINGS")
print("Activity 4 Number 6")
print(" The piece of code below will give an error when output; x = “All “Data Scientists” are cool!”  Write a python program to correct it.")
g = "'All \"Data scientists\" are cool!'"
print(g)
print("*****************************************************************************")

#Dicts
print("Activity 5 Dict")
#1
print("Activity 5 Dict")
print("Activity 5 Number 1")
print(" With reference to the dictionary below, write a python program to print the value of the shoe size. Add this dictionary to your .py fileShoes = {“brand” : “Nick”,“color” : “black”,“size” : 40}")
shoes ={
    "brand" : "Nike",
    "color" : "black",
    "size" : 40,
}
print(shoes["size"])
print("*****************************************************************************")

#2
print("Activity 5 Dict")
print("Activity 5 Number 2")
print("Write a python program to change the value “Nick” to “Adidas”")
shoes["brand"] = "Adidas"
print(shoes)
print("*****************************************************************************")

#3
print("Activity 5 Dict")
print("Activity 5 Number 3")
print(" Write a python program to add a key/value pair 'type': 'sneakers' to the dictionary")
shoes["type"] = "sneakers"
print(shoes)
print("*****************************************************************************")

#4
print("Activity 5 Dict")
print("Activity 5 Number 4")
print(" Write a python program to return a list of all the keys in the dictionary above.")
print(shoes.keys())
print("*****************************************************************************")

#5
print("Activity 5 Dict")
print("Activity 5 Number 5")
print("Write a python program to return a list of all the values in the dictionary above.")
print(shoes.values())
print("*****************************************************************************")

#6
print("Activity 5 Dict")
print("Activity 5 Number 6")
print("Check if the key “size” exists in the dictionary above")
if "size" in shoes.keys():
    print("YES")
else:
    print("NO")
print("*****************************************************************************")

#7
print("Activity 5 Dict")
print("Activity 5 Number 7 ")
print("Write a python program to loop through the dictionary above")
for t in shoes:
    print(t)
print("*****************************************************************************")

#8
print("Activity 5 Dict")
print("Activity 5 Number 8")
print("Write a python program to remove “color” from the dictionary")
shoes.pop("color")
print(shoes)
print("*****************************************************************************")

#9
print("Activity 5 Dict")
print("Activity 5 Number 9")
print(" Write a python program to empty the dictionary above.")
shoes.clear()
print(sho4es)
print("*****************************************************************************")

#10
print("Activity 5 Dict")
print("Activity 5 Number 10")
print("Write a dictionary of your choice and make a copy of it.")
num_to_word ={
    1:"one",
    2:"two"
}
num_to_word2 = num_to_word.copy()
print(num_to_word)
print(num_to_word2)
print("*****************************************************************************")

#11
print("Activity 5 Dict")
print("Activity 5 Number 11")
print(" Write a python program to show nested dictionaries")
anime1 = {
    "name": "attack on titan",
    "episodes": 87
}
anime2 = {
    "name": "drifters",
    "episodes": 12
}
anime3 = {
    "name": "demon slayer",
    "episodes": 42
}

mycollection = {
    "anime1": anime1,
    "anime2": anime2,
    "anime3": anime3
}

print(mycollection["anime1"]["episodes"])
print("*****************************************************************************")
#12
print("Activity 5 Dict")
print("Activity 5 Number 12")

for x in mycollection:
    for y in mycollection[x]:
        print(mycollection[x][y])

