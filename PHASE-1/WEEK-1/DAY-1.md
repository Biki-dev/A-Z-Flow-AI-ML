## 1. Types

Python has several built-in data types.

| Category | Types | Example |
|---|---|---|
| Text | `str` | `x = "Hello"` |
| Numeric | `int`, `float`, `complex` | `x = 20`, `x = 20.5`, `x = 1j` |
| Sequence | `list`, `tuple`, `range` | `x = [1, 2]` |
| Mapping | `dict` | `x = {"name": "Biki"}` |
| Set | `set`, `frozenset` | `x = {1, 2, 3}` |
| Boolean | `bool` | `x = True` |
| Binary | `bytes`, `bytearray`, `memoryview` | `x = b"Hi"` |
| None | `NoneType` | `x = None` |

### Check Type

```python
x = 20
print(type(x))
# <class 'int'>
```

---

# 2. Variables

A variable stores a value.

```python
x = "Hello"
age = 20
price = 20.5
```

### Multiple Variables

```python
x, y, z = "Apple", "Banana", "Cherry"
```

### Same Value

```python
x = y = z = "Orange"
```

### Rules for Variable Names

* Start with a letter or `_`
* Cannot start with a number
* Can contain letters, numbers and `_`
* Case-sensitive
* Cannot use Python keywords

```python
my_var = 10
_my_var = 20
myVar = 30
my_var2 = 40
```

---

# 3. Control Flow

Control flow decides **which code runs and in what order**.

## Conditional Statements

### `if`

```python
age = 20

if age >= 18:
    print("Adult")
```

### `if ... else`

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### `if ... elif ... else`

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

### Nested `if`

```python
age = 20
citizenship = "Indian"

if age >= 18:
    if citizenship == "Indian":
        print("Eligible")
```

---

## `match`

Useful when comparing one value against multiple cases.

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid")
```

---

# 4. Loops

## `for`

Used to iterate over a sequence.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### `range()`

```python
for i in range(5):
    print(i)
# 0 1 2 3 4
```

## `while`

Runs while the condition is `True`.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# 5. Loop Control

| Keyword    | Meaning                  |
| ---------- | ------------------------ |
| `break`    | Stop the loop            |
| `continue` | Skip current iteration   |
| `pass`     | Do nothing / placeholder |

### `break`

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### `continue`

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### `pass`

```python
for i in range(5):
    pass
```

---

# 6. Ternary Expression

One-line `if ... else`.

```python
age = 20

status = "Adult" if age >= 18 else "Minor"
```

---

# 7. Python Collections

The four important collections:

```text
list   → ordered + mutable
tuple  → ordered + immutable
set    → unique + fast membership
dict   → key → value
```

---

# 8. List

A `list` is:

* Ordered
* Mutable
* Allows duplicates
* Supports indexing and slicing

```python
fruits = ["apple", "banana", "apple"]

print(fruits[0])
# apple
```

### Common Operations

```python
fruits.append("mango")
fruits.insert(1, "grape")
fruits.remove("apple")
fruits.pop()
fruits.sort()
fruits.reverse()
```

### Use List When

```text
✓ Order matters
✓ Need indexing
✓ Duplicates are allowed
✓ Need to modify the sequence
```

Example:

```python
tasks = ["study", "code", "exercise"]
```

---

# 9. Tuple

A `tuple` is:

* Ordered
* Immutable
* Allows duplicates
* Supports indexing and slicing

```python
point = (10, 20)
```

Cannot modify:

```python
point[0] = 50
# TypeError
```

### Tuple Unpacking

```python
person = ("Biki", 20)

name, age = person
```

### Use Tuple When

```text
✓ Order matters
✓ Data should not change
✓ Representing fixed values
```

Examples:

```python
coordinates = (10, 20)
rgb = (255, 128, 0)
```

---

# 10. Set

A `set` stores **unique values**.

```python
numbers = {10, 20, 30, 20, 10}

print(numbers)
# {10, 20, 30}
```

### Properties

* Unique values only
* Mutable
* No indexing
* Unordered
* Fast membership testing

### Membership

```python
fruits = {"apple", "banana", "cherry"}

print("apple" in fruits)
# True
```

### Add / Remove

```python
fruits.add("mango")
fruits.remove("banana")
```

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b    # Union → {1, 2, 3, 4, 5}
a & b    # Intersection → {3}
a - b    # Difference → {1, 2}
a ^ b    # Symmetric difference → {1, 2, 4, 5}
```

---

# 11. Set vs List — IMPORTANT

The key question is:

> **Do I need to store a sequence, or do I mainly need to check whether something exists?**

### List

```python
users = ["Amit", "Rahul", "Biki", "John"]

"Biki" in users
```

Average membership lookup:

```text
O(n)
```

Python may need to check elements one by one.

### Set

```python
users = {"Amit", "Rahul", "Biki", "John"}

"Biki" in users
```

Average membership lookup:

```text
O(1)
```

Sets use hashing, making membership checks very fast on average.

### Choose Set When

```text
✓ Need unique values
✓ Frequently use `x in collection`
✓ Order is not important
✓ Need set operations
```

Example:

```python
blocked_users = {"user1", "user2", "user3"}

if username in blocked_users:
    print("Blocked")
```

### Choose List When

```text
✓ Order matters
✓ Need indexing
✓ Duplicates matter
✓ Working with a sequence
```

---

# 12. Dictionary

A `dict` stores:

```text
key → value
```

```python
student = {
    "name": "Biki",
    "age": 20,
    "branch": "Mechanical"
}
```

### Access

```python
student["name"]
student.get("name")
```

### Add / Update

```python
student["age"] = 21
student["college"] = "AEC"
```

### Delete

```python
del student["age"]
```

### Check Key

```python
if "name" in student:
    print("Exists")
```

### Loop

```python
for key, value in student.items():
    print(key, value)
```

### Useful Methods

```python
student.keys()
student.values()
student.items()
student.get("name")
student.update({"age": 21})
student.pop("age")
```

### Dictionary Lookup

Average key lookup:

```text
O(1)
```

---

# 13. Common Data Structures

### List of Dictionaries

Useful for multiple records/objects.

```python
students = [
    {"name": "Biki", "age": 20},
    {"name": "Rahul", "age": 21},
    {"name": "Amit", "age": 19}
]

print(students[0]["name"])
# Biki
```

### Dictionary of Lists

```python
courses = {
    "Python": ["Biki", "Rahul", "Amit"],
    "Java": ["John", "Alex"]
}
```

---

# 14. Collection Decision Guide

| Need                       | Use              |
| -------------------------- | ---------------- |
| Ordered sequence           | `list`           |
| Fixed / immutable sequence | `tuple`          |
| Unique values              | `set`            |
| Fast membership check      | `set`            |
| Key → value lookup         | `dict`           |
| Index-based access         | `list` / `tuple` |
| Duplicates allowed         | `list` / `tuple` |

---

# 15. Big-O Revision

| Operation       |  List | Tuple |   Set |  Dict |
| --------------- | ----: | ----: | ----: | ----: |
| Index access    |  O(1) |  O(1) |     ❌ |     ❌ |
| Membership `in` |  O(n) |  O(n) | O(1)* | O(1)* |
| Append          | O(1)* |     ❌ | O(1)* | O(1)* |
| Insert          |  O(n) |     ❌ |     — |     — |
| Delete          |  O(n) |     ❌ | O(1)* | O(1)* |

`*` = average / amortized complexity.

---

# 16. Final Memory Trick

```text
LIST
→ Ordered
→ Mutable
→ Duplicates
→ Indexing

TUPLE
→ Ordered
→ Immutable
→ Fixed data

SET
→ Unique
→ No indexing
→ Fast `in`
→ O(1) average lookup

DICT
→ Key → Value
→ Fast key lookup
→ O(1) average lookup
```

## The Most Important Decision

```text
Need order?             → LIST
Need fixed data?        → TUPLE
Need uniqueness?        → SET
Need fast `x in`?       → SET
Need key → value?       → DICT
```
