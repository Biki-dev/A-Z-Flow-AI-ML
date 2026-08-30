# Day 3 — Iteration & Comprehensions

Learn to write **cleaner, shorter Python code** instead of using raw `for` loops everywhere.

---

# 1. List Comprehension

A list comprehension creates a new list in **one line**.

### Basic Syntax

```python
[expression for item in iterable]
```

### Normal Loop

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for n in numbers:
    squares.append(n * n)
```

### List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [n * n for n in numbers]
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

# 2. List Comprehension with Condition

### Syntax

```python
[expression for item in iterable if condition]
```

### Example

```python
numbers = [1, 2, 3, 4, 5, 6]

even = [n for n in numbers if n % 2 == 0]

print(even)
# [2, 4, 6]
```

### `if ... else`

```python
numbers = [1, 2, 3, 4, 5]

result = ["even" if n % 2 == 0 else "odd" for n in numbers]
```

Output:

```text
['odd', 'even', 'odd', 'even', 'odd']
```

---

# 3. Dictionary Comprehension

Creates a dictionary using a compact syntax.

### Syntax

```python
{key: value for item in iterable}
```

### Example

```python
numbers = [1, 2, 3, 4, 5]

squares = {n: n * n for n in numbers}

print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### With Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    n: n * n
    for n in numbers
    if n % 2 == 0
}
```

Result:

```text
{2: 4, 4: 16, 6: 36}
```

---

# 4. Set Comprehension

Same idea, but creates a `set`.

```python
numbers = [1, 2, 2, 3, 3, 4]

squares = {n * n for n in numbers}

print(squares)
# {1, 4, 9, 16}
```

Useful when you need **unique results**.

---

# 5. `enumerate()`

Use `enumerate()` when you need both:

```text
index + value
```

### Without `enumerate()`

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, fruits[i])
```

### With `enumerate()`

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
```

Output:

```text
0 apple
1 banana
2 cherry
```

### Start Index

```python
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
```

Output:

```text
1 apple
2 banana
3 cherry
```

### Remember

```text
enumerate(iterable)
→ index + value
```

---

# 6. `zip()`

`zip()` combines multiple iterables element-by-element.

```python
names = ["Biki", "Rahul", "Amit"]
ages = [20, 21, 19]

for name, age in zip(names, ages):
    print(name, age)
```

Output:

```text
Biki 20
Rahul 21
Amit 19
```

### Remember

```text
zip()
→ combine corresponding elements
```

---

# 7. `zip()` with Different Lengths

`zip()` stops when the **shortest iterable** ends.

```python
names = ["Biki", "Rahul", "Amit"]
ages = [20, 21]

print(list(zip(names, ages)))
```

Output:

```text
[('Biki', 20), ('Rahul', 21)]
```

---

# 8. `enumerate()` + `zip()`

Very useful in real code.

```python
names = ["Biki", "Rahul", "Amit"]
scores = [90, 85, 95]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(i, name, score)
```

Output:

```text
1 Biki 90
2 Rahul 85
3 Amit 95
```

---

# 9. Convert `zip()` to Dictionary

A common pattern:

```python
names = ["Biki", "Rahul", "Amit"]
scores = [90, 85, 95]

result = dict(zip(names, scores))

print(result)
```

Output:

```text
{
    'Biki': 90,
    'Rahul': 85,
    'Amit': 95
}
```

---

# 10. Nested List Comprehension

Useful for working with nested data.

### Example

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

values = [x for row in matrix for x in row]

print(values)
# [1, 2, 3, 4, 5, 6]
```

Read it as:

```text
for each row
    for each x in row
        add x
```

---

# 11. When to Use Comprehensions

Use comprehensions when the logic is:

```text
✓ Short
✓ Simple
✓ Easy to read
✓ Mainly transforming or filtering data
```

Good:

```python
squares = [x * x for x in numbers]
```

Avoid overly complicated comprehensions:

```python
# Hard to read
result = [x * 2 if x > 5 else x / 2 for x in numbers if x % 2 == 0]
```

A normal loop may be clearer when the logic becomes complex.

---

# 12. Raw Loop vs Comprehension

### Raw Loop

```python
result = []

for x in numbers:
    if x % 2 == 0:
        result.append(x * x)
```

### Comprehension

```python
result = [x * x for x in numbers if x % 2 == 0]
```

### Mental Pattern

```text
[WHAT_TO_STORE
 FOR WHAT_TO_ITERATE
 IF CONDITION]
```

---

# 13. Common Python Iteration Tools

| Tool               | Purpose                  |
| ------------------ | ------------------------ |
| `for`              | Iterate through items    |
| `range()`          | Generate number sequence |
| `enumerate()`      | Get index + value        |
| `zip()`            | Combine iterables        |
| List comprehension | Create a list            |
| Dict comprehension | Create a dictionary      |
| Set comprehension  | Create a set             |

---

# 14. AI/ML Examples

Comprehensions are especially useful for **data preprocessing**.

### Transform Data

```python
prices = [100, 200, 300]

normalized = [p / 100 for p in prices]
```

### Filter Data

```python
ages = [12, 18, 25, 15, 30]

adults = [age for age in ages if age >= 18]
```

### Extract Values

```python
students = [
    {"name": "Biki", "score": 90},
    {"name": "Rahul", "score": 85},
    {"name": "Amit", "score": 95}
]

scores = [student["score"] for student in students]
```

### Create Mapping

```python
scores = {
    student["name"]: student["score"]
    for student in students
}
```

---

# 15. Revision Cheat Sheet

```text
LIST COMPREHENSION
→ Create / transform a list

[x * 2 for x in numbers]


DICT COMPREHENSION
→ Create / transform a dictionary

{x: x * x for x in numbers}


SET COMPREHENSION
→ Create unique results

{x * x for x in numbers}


enumerate()
→ index + value

for i, x in enumerate(items):
    ...


zip()
→ combine corresponding items

for a, b in zip(list1, list2):
    ...


range()
→ generate number sequence

for i in range(5):
    ...
```

# Final Memory Trick

```text
Need a new LIST?      → list comprehension
Need a new DICT?      → dict comprehension
Need unique results?  → set comprehension
Need INDEX + VALUE?   → enumerate()
Need to COMBINE?      → zip()
Need NUMBERS?         → range()
```
