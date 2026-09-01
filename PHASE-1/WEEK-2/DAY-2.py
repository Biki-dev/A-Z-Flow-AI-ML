# Python OOP — Class Variables

# Instance variable:
# Unique to each object; usually defined using self inside __init__().

# Class variable:
# Shared by all instances of a class.
# Defined directly inside the class.

class Employee:

    raise_amount = 1.04      # Class variable
    num_of_employees = 0     # Class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Biki', 'Kalita', 20000)
emp_2 = Employee('Ram', 'Kalita', 50000)

# Class variable can be accessed through class:
# Employee.raise_amount

# Or through an instance:
# emp_1.raise_amount

# Instance lookup:
# Python first checks the instance, then the class.

# Changing through class affects all instances:
# Employee.raise_amount = 1.05

# Changing through instance creates/overrides
# that variable for only that instance:
# emp_1.raise_amount = 1.05

# __dict__ shows attributes stored in an object/class:
# emp_1.__dict__
# Employee.__dict__

# Use Employee.num_of_employees when tracking
# a value common to the whole class.

# Use self.raise_amount when allowing individual
# instances/subclasses to override the class value.