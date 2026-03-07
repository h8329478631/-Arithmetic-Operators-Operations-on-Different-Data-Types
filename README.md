# Python Arithmetic Operators with All Data Types

## 📌 Project Description

This project demonstrates how **Python arithmetic operators** behave with different **fundamental and collective data types**.

The program shows:

* Which operations work
* Which operations produce **TypeError**
* Which operations produce **ZeroDivisionError**

This helps beginners understand **how Python handles arithmetic operations between different data types**.

---

# 🔢 Arithmetic Operators Used

Python has **6 arithmetic operators**:

| Operator | Meaning        |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `//`     | Floor Division |
| `%`      | Modulus        |

---

# 📚 Data Types Covered

## Fundamental Data Types

* `int`
* `float`
* `bool`
* `complex`
* `string`

## Collective Data Types

* `list`
* `tuple`
* `set`
* `frozenset`
* `dictionary`

---

# ⚙️ Operations Demonstrated

The program performs arithmetic operations on:

### 1️⃣ Integer Operations

Examples:

* int + int
* int - int
* int * int
* int / int
* int // int
* int % int

---

### 2️⃣ Boolean Operations

Python treats:

* `True = 1`
* `False = 0`

Examples:

```
True + True = 2
True * False = 0
```

Some operations produce **ZeroDivisionError** when dividing by `False`.

---

### 3️⃣ String Operations

Allowed:

```
string + string  → concatenation
```

Not Allowed:

```
string - string
string * string
string / string
```

These produce **TypeError**.

---

### 4️⃣ Float Operations

All arithmetic operators work with floats.

Example:

```
4.0 + 5.0 = 9.0
5.0 / 4.0 = 1.25
```

---

### 5️⃣ Complex Number Operations

Allowed:

```
+
-
*
/
```

Not Allowed:

```
//
%
```

---

### 6️⃣ List Operations

Allowed:

```
list + list → concatenation
```

Example:

```
[1,2,3] + [4,5,6]
```

Not allowed:

```
-
*
/
```

---

### 7️⃣ Tuple Operations

Same behavior as lists.

Allowed:

```
tuple + tuple
```

Not allowed:

```
-
*
/
```

---

### 8️⃣ Set Operations

Arithmetic operators are **not supported** on sets.

All operations produce **TypeError**.

---

### 9️⃣ Frozenset Operations

Same as sets.

All arithmetic operators produce **TypeError**.

---

### 🔟 Dictionary Operations

Arithmetic operators are **not supported**.

All operations result in **TypeError**.

---

# 🔄 Cross Datatype Operations

The project also demonstrates operations like:

```
int + bool
int + float
int + complex
int + string
int + list
int + tuple
int + set
int + frozenset
int + dictionary
```

This helps understand **which combinations are valid in Python**.

---

# ▶️ How to Run

1. Clone the repository

```
git clone https://github.com/your-username/your-repository.git
```

2. Open the project in **VS Code**

3. Run the file

```
python operators.py
```

---

# 🎯 Learning Outcome

After running this project you will understand:

* Python arithmetic operator behavior
* Data type compatibility
* TypeError cases
* ZeroDivisionError cases
* How Python handles mixed data types

---

# 👨‍💻 Author

Harshal Warke
