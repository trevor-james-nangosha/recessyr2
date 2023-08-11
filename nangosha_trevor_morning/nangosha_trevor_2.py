age =21
if age < 18:
    print("You are underage")
elif age >= 18 and age <= 65:
    print("You are an adult")
else:
    print("You are a senior citizen")

#Loops
#loops(for and while)

#for items in squence
cars = ["cars", "jeep", "ford", "bmw"]
for car in cars:
    print(car)

fruits = ["mango", "orange", "banana"]
for friut in fruits:
    print(friut)

set = {"math", "phy", "sci"}
for i in set:
    print(i)

#while loops
#while condition is true: it will execute code hile condition is true

x=0
while x < 5:
    print(x)
    x += 1


fruits = ["mango", "orange", "banana"]
friut_count = 0
while friut_count < len(fruits):
    print(fruits[friut_count])
    friut_count += 1



try:
    f = 10/0
except ZeroDivisionError:
    print("error")
finally:
    print("yes")