# Day 4 — Error Handling & File I/O

Learn to make programs **handle errors safely** and **read/write data from files**.

---

# 1. Error Handling

Errors can stop a program unexpectedly.

Python uses:

```text
try
except
else
finally
```

---

## `try / except`

Put risky code inside `try`.

```python
try:
    x = 10 / 0
except:
    print("Something went wrong")
```

### Better: Catch Specific Errors

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Common Exceptions

| Exception           | Example                  |
| ------------------- | ------------------------ |
| `ValueError`        | Invalid value conversion |
| `TypeError`         | Wrong data type          |
| `KeyError`          | Missing dictionary key   |
| `IndexError`        | Invalid list index       |
| `FileNotFoundError` | File does not exist      |
| `ZeroDivisionError` | Division by zero         |

---

# 2. Multiple `except`

Handle different errors separately.

```python
try:
    x = int(input("Enter number: "))
    result = 10 / x

except ValueError:
    print("Enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 3. `else`

`else` runs **only when no exception occurs**.

```python
try:
    x = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Success:", x)
```

---

# 4. `finally`

`finally` runs **whether an error occurs or not**.

```python
try:
    x = 10 / 2

except ZeroDivisionError:
    print("Error")

finally:
    print("This always runs")
```

Useful for cleanup operations.

---

# 5. Complete Error Handling

```python
try:
    x = int(input("Enter number: "))
    result = 100 / x

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program finished")
```

### Remember

```text
try     → risky code
except  → handle error
else    → runs if no error
finally → always runs
```

---

# 6. Get the Error Message

Use `as e`.

```python
try:
    x = int("hello")

except ValueError as e:
    print(e)
```

---

# 7. File I/O

File I/O means:

```text
I/O = Input / Output
```

Python can:

```text
Read files
Write files
Append files
```

The basic tool is:

```python
open()
```

---

# 8. Opening a File

```python
file = open("data.txt", "r")
```

Common modes:

| Mode  | Meaning           |
| ----- | ----------------- |
| `"r"` | Read              |
| `"w"` | Write / overwrite |
| `"a"` | Append            |
| `"x"` | Create new file   |

---

# 9. `with open()`

Preferred way to work with files because Python automatically closes the file.

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

### Remember

```text
with open(...)
→ automatically closes the file
```

---

# 10. Reading a Text File

### Read Entire File

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

### Read One Line

```python
with open("data.txt", "r") as file:
    line = file.readline()
```

### Read All Lines

```python
with open("data.txt", "r") as file:
    lines = file.readlines()
```

---

# 11. Writing a Text File

`"w"` creates the file if needed and **overwrites existing content**.

```python
with open("data.txt", "w") as file:
    file.write("Hello World")
```

---

# 12. Appending to a File

`"a"` adds content to the end.

```python
with open("data.txt", "a") as file:
    file.write("\nHello Again")
```

---

# 13. JSON

JSON is commonly used for **structured data** and APIs.

Python has a built-in:

```python
import json
```

Example JSON:

```json
{
    "name": "Biki",
    "age": 20,
    "skills": ["Python", "ML"]
}
```

---

# 14. Write JSON

Use `json.dump()` to write Python data to a file.

```python
import json

student = {
    "name": "Biki",
    "age": 20,
    "skills": ["Python", "ML"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

---

# 15. Read JSON

Use `json.load()`.

```python
import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student["name"])
# Biki
```

---

# 16. JSON — Python Conversion

```text
Python                  JSON
--------------------------------
dict        ↔           object
list        ↔           array
str         ↔           string
int/float   ↔           number
True        ↔           true
False       ↔           false
None        ↔           null
```

### Important Functions

```text
json.dump() → Python → JSON file
json.load() → JSON file → Python
json.dumps() → Python → JSON string
json.loads() → JSON string → Python
```

---

# 17. CSV

CSV = **Comma-Separated Values**

Example:

```csv
name,age,score
Biki,20,90
Rahul,21,85
Amit,19,95
```

Python has a built-in:

```python
import csv
```

---

# 18. Write CSV

Use `csv.writer`.

```python
import csv

rows = [
    ["name", "age", "score"],
    ["Biki", 20, 90],
    ["Rahul", 21, 85],
    ["Amit", 19, 95]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

---

# 19. Read CSV

```python
import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

# 20. CSV with Dictionaries

Useful when CSV has column names.

### Write

```python
import csv

students = [
    {"name": "Biki", "age": 20, "score": 90},
    {"name": "Rahul", "age": 21, "score": 85}
]

with open("students.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "score"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(students)
```

### Read

```python
import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["score"])
```

---

# 21. JSON vs CSV

| Feature        | JSON                           | CSV               |
| -------------- | ------------------------------ | ----------------- |
| Structure      | Nested / hierarchical          | Tabular           |
| Best for       | APIs, configs, structured data | Tables / datasets |
| Python library | `json`                         | `csv`             |
| Nested data    | ✅                              | ❌                 |
| Human-readable | ✅                              | ✅                 |

### Typical Use

```text
JSON → API responses, configurations, metadata
CSV  → datasets, spreadsheets, tabular data
```

---

# 22. Error Handling + File I/O

Real programs should handle missing or invalid files.

```python
import json

try:
    with open("student.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    print("File not found")

except json.JSONDecodeError:
    print("Invalid JSON")

else:
    print(data)

finally:
    print("Finished")
```

---

# 23. AI/ML Relevance

File I/O is used constantly in ML work.

```text
CSV  → datasets
JSON → configuration / metadata / API data
TXT  → logs / text data
```

Example:

```python
import csv

with open("training_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

---

# 24. Revision Cheat Sheet

```text
ERROR HANDLING
try      → risky code
except   → handle exception
else     → runs if successful
finally  → always runs

FILE I/O
open()   → open file
"r"      → read
"w"      → overwrite/write
"a"      → append
with     → automatically closes file

JSON
json.dump()  → Python → JSON file
json.load()  → JSON file → Python
json.dumps() → Python → JSON string
json.loads() → JSON string → Python

CSV
csv.reader()      → read rows
csv.writer()      → write rows
csv.DictReader()  → read rows as dictionaries
csv.DictWriter()  → write dictionaries
```

# Final Memory Trick

```text
Need to handle failure?       → try / except

Need cleanup always?          → finally

Need a plain text file?       → open()

Need structured data/API?     → JSON

Need tabular data/dataset?    → CSV

JSON → nested / structured
CSV  → rows / columns
```
