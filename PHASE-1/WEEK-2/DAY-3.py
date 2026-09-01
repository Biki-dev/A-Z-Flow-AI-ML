# ============================================================
# PYTHON OOP — INSTANCE, CLASS & STATIC METHODS
# ============================================================


class Employee:

    # CLASS VARIABLES
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        # INSTANCE VARIABLES
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        # Access class variable
        Employee.num_of_emps += 1

    # --------------------------------------------------------
    # INSTANCE METHOD
    # --------------------------------------------------------

    def fullname(self):
        # `self` = current object
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    # --------------------------------------------------------
    # CLASS METHOD
    # --------------------------------------------------------

    @classmethod
    def set_raise_amt(cls, amount):
        # `cls` = class itself
        cls.raise_amt = amount


    # CLASS METHOD AS ALTERNATIVE CONSTRUCTOR
    @classmethod
    def from_string(cls, emp_str):
        # Another way to create Employee objects
        first, last, pay = emp_str.split('-')

        # cls(...) creates and returns an object
        return cls(first, last, pay)


    # --------------------------------------------------------
    # STATIC METHOD
    # --------------------------------------------------------

    @staticmethod
    def is_workday(day):
        # No `self` and no `cls`
        # Works only with the data passed to it

        if day.weekday() == 5 or day.weekday() == 6:
            return False

        return True


# ============================================================
# OBJECT CREATION
# ============================================================

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# Each object has its own instance variables.


# ============================================================
# CLASS METHOD
# ============================================================

Employee.set_raise_amt(1.05)

# Changes the shared class variable
# Employee.raise_amt -> 1.05
# emp_1.raise_amt     -> 1.05
# emp_2.raise_amt     -> 1.05


# ============================================================
# ALTERNATIVE CONSTRUCTOR
# ============================================================

emp_str_1 = 'John-Doe-70000'

# Normal way:
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# Using class method:
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


# ============================================================
# STATIC METHOD
# ============================================================

import datetime

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

# Monday-Friday -> True
# Saturday-Sunday -> False


# ============================================================
# QUICK REFERENCE
# ============================================================

# Instance Method
# -> self
# -> works with instance/object
# -> Example: fullname(), apply_raise()

# Class Method
# -> @classmethod
# -> cls
# -> works with class
# -> Example: set_raise_amt()

# Alternative Constructor
# -> class method
# -> Example: from_string()

# Static Method
# -> @staticmethod
# -> no self / no cls
# -> utility function related to class
# -> Example: is_workday()


# MEMORY:
# self -> Object
# cls  -> Class
# staticmethod -> Neither