# Python OOP
# Class = blueprint for objects
# Object/Instance = object created from a class
# Attribute = variable/data inside an object
# Method = function inside a class
# __init__() = runs automatically when object is created
# self = refers to the current object
# Instance variables = unique for each object
# Method call: emp_1.fullname()
# Equivalent: Employee.fullname(emp_1)

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Biki', 'Kalita', 20000)
emp_2 = Employee('Ram', 'Kalita', 50000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())

# Calling method using class:
print(Employee.fullname(emp_1))