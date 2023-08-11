# Activity1 {Use the len() with tuples }
#Activity2 {Accessing Tuples, indexing, ranges }

phones = ("samsung", "iphone", "tecno")
# Use the len()
length = len(phones)
print(length)

#Accessing Tuples using index
phone = ("samsung", "iphone", "tecno")
l = phone[1]
e = phone[2]
print(l)
print(e)

#Using Ranges
t = phone[0:3]
w = phone[0:]
x = phone[:2]
print(t)
print(w)
print(x)


#Activity find the lenght of set, datatype, accessing items in a set, adding items, add two sets together
setone = {"rice", "matooke", "irish","potato"}
print(setone)

# Getting the length
Length = len(setone)
print(Length)

#Datatype
print(type(setone))

#Accessing iteems
for i in setone:
    print(i)

#Adding items
setone.add('cassava')
print(setone)

#Adding two sets
settwo = {"meat", "fish"}

setthree = setone.union(settwo)
print(setthree)