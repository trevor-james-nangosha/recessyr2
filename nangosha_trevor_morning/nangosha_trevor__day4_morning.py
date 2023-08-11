""""
# class
# Example1

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_enginee(self):
        print("Engine started")

    def stop_enginee(self):
        print("Engine stopped")


my_car = car("toyota", "corola", 2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)

my_car.start_enginee()
my_car.stop_enginee()


# Example 2: Bank Account
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # def deposit(self):


# example3


class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def cal_area(self):
        return self.length * self.width

    def cal_perm(self):
        return 2 * (self.width + self.length)


# creating an object
my_rec = rectangle(15, 5)
print(my_rec.length)
print(my_rec.width)

# calling out print methods
print(my_rec.cal_area())


# example 4
class student:
    def __init__(self, name, year, coruse):
        self.name = name
        self.year = year
        self.coruse = coruse

    def display_details(self):
        print("name", self.name)
        print("year", self.year)
        print("course", self.coruse)


# creat an object
my_stdent = student("mike", 3, "software")

# display stedent details
my_stdent.display_details()


# Object

class Person:
    def __init__(self, names, age):
        self.names = names
        self.age = age

    def greet(self):
        print("Hello, my name is ", self.names)
        print("i am", self.age, "years old")


# creat object
my_person = Person("Jeff Geoff", 35)
my_person2 = Person("Trevour", 25)

# Display the Person details
print(my_person.names)
print(my_person.age)

print(my_person2.names)
print(my_person2.age)

my_person.greet()
my_person2.greet()


# Activity1 Calculate the area and circmference of a circle
# Activity2  2 employees calculate bouns (0.5 of salary){employee1 salary 150000, employee2 salary 230000}

class Employee_bonus:
    def __init__(self, employee_name, salary):
        self.employee_name = employee_name
        self.salary = salary

    def bonus(self):
        bonus_answer = 0.15 * self.salary
        print("Your name is", self.employee_name, "with a salary ", self.salary, "of and your bonus is ", bonus_answer)


my_employee = Employee_bonus("Mike", 150000)
my_employee.bonus()
my_employee2 = Employee_bonus("Mic", 230000)
my_employee2.bonus()


# Encapsulation
# main goals of encapslation
# 1 to hide the implementation of an object
# 2 to protect the object from changes
# 3

# example with a bank account
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # encapsulate account number
        self._balance = balance  # encapslate balance

    def depoist(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("insufficent fnds")

    def get_balance(self):
        return self._balance()

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance


# create object
my_account = BankAccount("123456789", 1000)

print(my_account.account_number)
print(my_account.balance)
my_account.depoist(500)
print(my_account.balance)
my_account.withdraw(100)
print(my_account.balance)


# Activity Convert temperature(37 celsius) from celsius to fahrenheit

class convert:
    def __init__(self, temp):
        self._temp = temp

    def fahr(self):
        return (self._temp * 9 / 5) + 32
        # con = (self._temp * 9/5) + 32
        # print(con)


temperature = convert(37)
temperature._temp = 100
print(temperature.fahr())
"""


# Activity 2 show encapsulation with employee information to give a pay increamentation (salary with employee information to new salary)
# eg from 850000 to 1000000

class increment:
    def __init__(self, employee_name, salary):
        self._employee_name = employee_name
        self._salary = salary

    def amount_increased(self, _increase):
        _amount = self._salary + _increase
        print("Employee Name: ",self._employee_name)
        print("Empolyee Salary: ",self._salary)
        print(
            f"Your Employee Name is {self._employee_name} and your Salary is {self._salary} and your Salary Increament is {_increase} hence your new salary is {_amount} ")
        print("Your New Salary is :",_amount)

# Create an employee object
Increment = increment("nangosha trevor", 850000)
Increment.amount_increased(150000)
