# Ordered and changeable and don't allo duplicates
# Used to store data vaules in key:values pairs
# Dicts can have data of different datatypes

mydict = {
    "phone" : "iphone",
    "iphonemodel" : "iphone15",
    "year" : 2023
}
print(mydict)

#length of dict
print(len(mydict))

#datatype
print(type(mydict))

#access dict items
z = mydict["year"]
print(z)

#using getter
y = mydict.get("iphonemodel")
print(y)
w = mydict.keys()
print(w)

#modify
s = mydict["iphonemodel"] = "iphone14"
print(s)

q = mydict.get("iphonemodel")
print(q)

#Acticity1 use te values() to return all values in a dic.
u = mydict.values()
print(u)

# Activity2 check if a key exicts in the dict
t = {
    "a" : 10,
    "b" : 9,
    "c" : 8,
}
if t.get("r") == None:
    print("Not Present")
else:
    print("Present")

# Activity3 how to change dict items, how to update,
#updating dic
dic = {
    "anime" : "attack on titan",
    "epispdes" : 87,
    "rating" : 10
}

dic1 = {
    "anime" : "attack",
    "epispdes" : 8,
    "rating" : 7
}
dic.update(dic1)
print(dic)

#changing dict
change = dic["epispdes"] = 88
print(change)


# Activity4 ho to add dict item, howw to remove items
# adding
dic.update( genre = "action")
print(dic)

# removing
dic2 = dic.pop("genre")
print(dic2) # item removed
print(dic) # dic after removing item

# Activity5 how to loop through a dict, how to nest a dict
for x in dic:
    print(x)

for y in dic:
    print(dic[y])

for z, f in dic.items():
    print(z,f)
# how to nest a dict
anime1 = {
    "name" : "attack on titan",
    "episodes" : 87
}
anime2 = {
    "name" : "drifters",
    "episodes" : 12
}
anime3 = {
    "name" : "demon slayer",
    "episodes" : 42
}

mycollection = {
    "anime1" : anime1,
    "anime2": anime2,
    "anime3": anime3
}

print(mycollection["anime1"]["episodes"])