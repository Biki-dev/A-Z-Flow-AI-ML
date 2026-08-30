# Day 2 — Functions & Scope

Functions let you **organize code into reusable blocks**.

---

# 1. Functions

## Define and Call a Function

```python
def greet():
    print("Hello!")

greet()
```

### Function with Parameters

```python
def greet(name):
    print("Hello", name)

greet("Biki")
```

### Return Value

`return` sends a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
# 30
```

### `print()` vs `return`

```text
print()  → displays a value
return   → sends a value back from the function
```

---

# 2. Parameters vs Arguments

```python
def add(a, b):        # a, b → parameters
    return a + b

add(10, 20)           # 10, 20 → arguments
```

---

# 3. Default Arguments

Give a parameter a default value.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
# Hello Guest

greet("Biki")
# Hello Biki
```

---

# 4. Keyword Arguments

Pass arguments using parameter names.

```python
def student(name, age):
    print(name, age)

student(age=20, name="Biki")
```

Useful when you want to make the meaning of arguments clear.

---

# 5. `*args`

`*args` allows a function to accept **any number of positional arguments**.

```python
def total(*args):
    return sum(args)

print(total(10, 20))
# 30

print(total(10, 20, 30, 40))
# 100
```

Inside the function, `args` is a **tuple**.

```python
def show(*args):
    print(args)

show(1, 2, 3)
# (1, 2, 3)
```

### Remember

```text
*args → variable number of positional arguments
```

---

# 6. `**kwargs`

`**kwargs` allows a function to accept **any number of keyword arguments**.

```python
def student(**kwargs):
    print(kwargs)

student(name="Biki", age=20, branch="Mechanical")
```

Output:

```text
{'name': 'Biki', 'age': 20, 'branch': 'Mechanical'}
```

Inside the function, `kwargs` is a **dictionary**.

### Remember

```text
**kwargs → variable number of keyword arguments
```

---

# 7. `*args` vs `**kwargs`

| Feature   | `*args`              | `**kwargs`        |
| --------- | -------------------- | ----------------- |
| Accepts   | Positional arguments | Keyword arguments |
| Stored as | Tuple                | Dictionary        |
| Example   | `f(1, 2, 3)`         | `f(a=1, b=2)`     |

### Together

```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(1, 2, 3, name="Biki", age=20)
```

---

# 8. Lambda Functions

A lambda is a **small anonymous function**.

### Normal Function

```python
def square(x):
    return x * x
```

### Lambda

```python
square = lambda x: x * x

print(square(5))
# 25
```

### Syntax

```text
lambda arguments : expression
```

### Example

```python
add = lambda a, b: a + b

print(add(10, 20))
# 30
```

Lambdas are mainly useful for **short, simple operations**.

---

# 9. Lambda with `sorted()`

A common real-world use:

```python
students = [
    {"name": "Biki", "age": 20},
    {"name": "Rahul", "age": 18},
    {"name": "Amit", "age": 22}
]

students.sort(key=lambda student: student["age"])
```

---

# 10. Scope

**Scope** determines where a variable can be accessed.

Main scopes to know:

```text
Local
Global
```

---

# 11. Local Scope

A variable created inside a function is **local to that function**.

```python
def my_function():
    x = 10
    print(x)

my_function()
```

`x` cannot normally be accessed outside the function:

```python
# print(x)
# NameError
```

---

# 12. Global Scope

A variable created outside a function is a **global variable**.

```python
x = 10

def my_function():
    print(x)

my_function()
```

The function can read the global variable.

---

# 13. Local vs Global

```python
x = 10

def my_function():
    x = 20
    print(x)

my_function()
print(x)
```

Output:

```text
20
10
```

Why?

```text
x inside function  → Local
x outside function → Global
```

The local variable does not change the global variable.

---

# 14. `global` Keyword

Use `global` when you need to **modify a global variable inside a function**.

```python
x = 10

def change():
    global x
    x = 20

change()

print(x)
# 20
```

### Important

Prefer returning values from functions instead of relying heavily on global variables.

Better:

```python
def change(x):
    return 20

x = change(x)
```

---

# 15. Modular Functions

A modular function should ideally:

```text
✓ Do one clear job
✓ Be reusable
✓ Accept inputs
✓ Return outputs
✓ Avoid unnecessary global state
```

### Bad

```python
def process():
    # 100 lines doing many unrelated things
    ...
```

### Better

```python
def load_data():
    ...

def clean_data(data):
    ...

def train_model(data):
    ...

def evaluate_model(model, data):
    ...
```

This becomes especially important in **AI/ML projects**.

---

# 16. Functions in an AI/ML Workflow

A typical ML program can be divided into functions:

```python
def load_data():
    ...

def preprocess(data):
    ...

def train_model(X, y):
    ...

def evaluate_model(model, X, y):
    ...
```

Then:

```python
data = load_data()
data = preprocess(data)

model = train_model(X, y)

evaluate_model(model, X_test, y_test)
```

This makes code easier to:

```text
Read
Test
Debug
Reuse
Maintain
```

---

# 17. Quick Revision Table

| Concept          | Remember                               |
| ---------------- | -------------------------------------- |
| `def`            | Define a function                      |
| `return`         | Send value back                        |
| Parameter        | Variable in function definition        |
| Argument         | Value passed to function               |
| Default argument | Parameter with default value           |
| `*args`          | Multiple positional arguments → tuple  |
| `**kwargs`       | Multiple keyword arguments → dict      |
| `lambda`         | Small anonymous function               |
| Local            | Variable inside function               |
| Global           | Variable outside function              |
| `global`         | Modify global variable inside function |

---

# 18. Most Important Syntax

```python
# Basic function
def add(a, b):
    return a + b


# Default argument
def greet(name="Guest"):
    return f"Hello {name}"


# *args
def total(*args):
    return sum(args)


# **kwargs
def info(**kwargs):
    return kwargs


# Lambda
square = lambda x: x * x


# Local variable
def test():
    x = 10


# Global variable
x = 10


# Modify global
def change():
    global x
    x = 20
```

---

# Final Memory Trick

```text
FUNCTION
→ Reusable block of code

return
→ Send result back

*args
→ positional → tuple

**kwargs
→ keyword → dict

lambda
→ short anonymous function

Local
→ inside function

Global
→ outside function

global
→ modify global variable
```

