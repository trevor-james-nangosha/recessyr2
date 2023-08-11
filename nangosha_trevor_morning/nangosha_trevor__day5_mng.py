# # Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name} is eating...")
#
#
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} is barking...Woof1")
#
# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} is meowing...")
#
# # create Animal object
# animal = Animal("Generic Animal")
# dog = Dog("Spot")
# cat = Cat("Fluffy")
#
# # Invoke call eat method
# animal.eat()
# dog.bark()
# dog.eat()
# cat.eat()
# cat.meow()
#
# # example 2
# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#
#     def display_infro(self):
#         print("Brand ", self.brand)
#         print("Color ", self.color)
#
#     def move(self):
#         print("Vehicle is moving")
#
# class Car(Vehicle):
#     def __init__(self,brand, color, num):
#         super().__init__(brand,color)
#         self.num = num
#
#     def display_infro(self):
#         super().display_infro()
#         print("kk", self.num)
#
#     def honk(self):
#         print(" you are honking")
#
# # car object
# my_car = Car("toyota", "red", 6)
#
# print("Brand:", my_car.brand)
# my_car.color
#
# # invoke the car methods
# my_car.display_infro()
# my_car.move()
# my_car.honk()
#
# # Activity use inhertance to calclate area and perimeter of a circle and rectangle Shape and Circle
#
# # multiple inheritances
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
#
# class flyable:
#     def fly(self):
#         print(f"{self.name} is flying")
#
# class Bird(Animal, flyable):
#     def __init__(self, name, species):
#         super().__init__(name)
#         self.species = species
#
#     def display_infro(self):
#         print(f"species: {self.species}")
#         print(f"Name: {self.name}")

# # create bird object
# my_bird = Bird("Pigeon","bird")
#
# my_bird.eat()
# my_bird.fly()
# my_bird.display_infro()
# class Shape:
#     def __init__(self, length, radius):
#         self.length = length
#         self.radius = radius
#
#     def area(self):
#         return
#
#     def perimeter(self):
#         return

# Method Overriding

class Animal:
    def make_sound(self):
        print("animal is making a sound")

class Dog(Animal):
    def make_sound(self):
        print("dog is barking")

class Cat(Animal):
    def make_sound(self):
        print("cat is meowing")

def make_animal_sound(animal):
    animal.make_sound()

# create object
animal = Animal()
dog = Dog()
cat = Cat()

# calling make_animal_sound function
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

dog.make_sound()

# Polymorphism
# allows 1 to write cod ethat can work with different objects
# Method Overriding: occurs when a derived class (child class) provides its own implementation of a method that is
# already defined in te base class/superclass

# Method Overloading: allowa a class to have multiple methods with the same name byt differnrt perimeter
# Example
# class Shape:
#     def calc_area(self):
#         pass
#
# class Rect(Shape):
#     def __init__(self,length, width):
#         self.length = length
#         self.width = width
#
#     def calc_area(self):
#         return self.length * self.width
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calc_area(self):
#         return 3.14 * self.radius**2
#
#     def calc_circ(self):
#         return 2*3.14 *self.radius
#
# # create object
# rect = Rect(5,5)
# circle = Circle(5)
#
# # calculate
# print("Area of rect", rect.calc_area())
# print('Area of circle', circle.calc_area())
# print(circle.calc_circ())

# Overloading example
class Cal:
    def add(self, x, y):
        return x*y

    def add(self, x, y, z):
        return x + y + z

# create object
cal = Cal()
#display output
print(cal.add(5,7))


# Abstraction
