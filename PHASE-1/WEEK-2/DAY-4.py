# ============================================================
# PYTHON OOP — INHERITANCE
# ============================================================

# INHERITANCE
# -> Child class inherits attributes/methods from parent class.
# -> Avoids repeating common code.
#
# Parent     -> Employee
# Child      -> Developer, Manager


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# ============================================================
# CHILD CLASS
# ============================================================

class Developer(Employee):
    pass

# Developer inherits everything from Employee.


dev_1 = Developer('Corey', 'Schafer', 50000)

print(dev_1.email)
print(dev_1.fullname())
dev_1.apply_raise()


# ============================================================
# METHOD RESOLUTION ORDER (MRO)
# ============================================================

# Python searches for methods/attributes in this order:
#
# Developer
#     ↓
# Employee
#     ↓
# object
#
# object = base class of all Python classes.

# Check MRO:
# print(Developer.__mro__)
# print(help(Developer))


# ============================================================
# OVERRIDING CLASS VARIABLES
# ============================================================

class Developer(Employee):

    raise_amt = 1.10

# Developer now uses 10% raise instead of Employee's 4%.
#
# Employee.raise_amt     -> 1.04
# Developer.raise_amt    -> 1.10
#
# Changing Developer does NOT change Employee.


# ============================================================
# ADDING NEW ATTRIBUTES
# ============================================================

class Developer(Employee):

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)

        # Developer-specific attribute
        self.programming_language = programming_language


dev_1 = Developer(
    'Corey',
    'Schafer',
    50000,
    'Python'
)

print(dev_1.email)
print(dev_1.programming_language)


# ============================================================
# super()
# ============================================================

# super() gives access to the parent class.
#
# Instead of repeating Employee.__init__ code:
#
# super().__init__(first, last, pay)
#
# Parent handles common attributes,
# child handles its own extra attributes.


# ============================================================
# MANAGER CLASS
# ============================================================

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        # Avoid mutable default argument like employees=[]
        self.employees = [] if employees is None else employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print('-->', employee.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

manager = Manager('Sue', 'Smith', 90000, [dev_1])

manager.add_employee(dev_2)
manager.remove_employee(dev_1)

manager.print_employees()


# ============================================================
# isinstance()
# ============================================================

# Checks whether an OBJECT is an instance of a class.

print(isinstance(manager, Manager))     # True
print(isinstance(manager, Employee))    # True
print(isinstance(manager, Developer))   # False


# ============================================================
# issubclass()
# ============================================================

# Checks whether a CLASS is a subclass of another class.

print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Employee))    # True
print(issubclass(Manager, Developer))   # False


# ============================================================
# QUICK REFERENCE
# ============================================================

# Parent Class
# -> Common/shared functionality
#
# Child Class
# -> Inherits parent functionality
# -> Can add new functionality
# -> Can override existing functionality
#
# super()
# -> Access parent class functionality
#
# isinstance(object, Class)
# -> Checks OBJECT relationship
#
# issubclass(Class, Parent)
# -> Checks CLASS inheritance relationship


# ============================================================
# MEMORY
# ============================================================

# Employee
#    │
#    ├── Developer
#    │
#    └── Manager
#
# Employee = common functionality
# Developer = employee + programming language
# Manager   = employee + managed employees