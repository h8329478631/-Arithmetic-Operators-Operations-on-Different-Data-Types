# Python Arithmetic Operators on Different Data Types

## 📌 Description
This project demonstrates how **Arithmetic Operators** work on different **Python Data Types**.  
It shows which operations are supported and which raise errors.

The program tests arithmetic operations on:

- Fundamental Data Types
- Collective Data Types

---

# Arithmetic Operators in Python

Python provides **6 Arithmetic Operators**:

| Operator | Name |
|--------|--------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| // | Floor Division |
| % | Modulus |

---

# Fundamental Data Types

## 1️⃣ Integer
All arithmetic operators work with integers.

Example:

```python
Int1 = 5
Int2 = 2

print(Int1 + Int2)   # 7
print(Int1 - Int2)   # 3
print(Int1 * Int2)   # 10
print(Int1 / Int2)   # 2.5
print(Int1 // Int2)  # 2
print(Int1 % Int2)   # 1
```

---

## 2️⃣ Boolean
In Python, **True = 1** and **False = 0**, so arithmetic operations are possible.

Example:

```python
bool1 = True
bool2 = False

print(bool1 + bool2)   # 1
print(bool1 - bool2)   # 1
print(bool1 * bool2)   # 0
```

⚠ Division by `False` causes **ZeroDivisionError**.

---

## 3️⃣ String
Only the **+ operator** works with strings (Concatenation).

Example:

```python
Str1 = "harshal"
Str2 = "warke"

print(Str1 + Str2)
```

Output:

```
harshalwarke
```

Other arithmetic operators will raise **TypeError**.

---

## 4️⃣ Float
All arithmetic operators work with floats.

Example:

```python
Float1 = 4.0
Float2 = 5.0

print(Float1 + Float2)
print(Float1 - Float2)
print(Float1 * Float2)
print(Float1 / Float2)
print(Float1 // Float2)
print(Float1 % Float2)
```

---

## 5️⃣ Complex Numbers

Supported Operators:

- Addition
- Subtraction
- Multiplication
- Division

Example:

```python
Comp1 = 5+10j
Comp2 = 3+8j

print(Comp1 + Comp2)
print(Comp1 - Comp2)
print(Comp1 * Comp2)
print(Comp1 / Comp2)
```

⚠ `//` and `%` do **not work with complex numbers**.

---

# Collective Data Types

## 1️⃣ List

Only **+ operator** works for lists.

It performs **concatenation** (combining lists).

Example:

```python
list1 = [1,2,3]
list2 = [4,5,6]

print(list1 + list2)
```

Output:

```
[1,2,3,4,5,6]
```

---

## 2️⃣ Tuple

Tuples also support **concatenation using +**.

Example:

```python
Tuple1 = (1,2,3)
Tuple2 = (4,5,6)

print(Tuple1 + Tuple2)
```

Output:

```
(1,2,3,4,5,6)
```

---

## 3️⃣ Set

Arithmetic operators **do not work with sets**.

Example:

```python
Set1 = {1,2,3}
Set2 = {4,5,6}
```

Using `+`, `-`, `*`, `/`, `//`, `%` will produce **TypeError**.

Sets use special methods like:

- union()
- intersection()

---

## 4️⃣ Frozenset

Frozenset is an **immutable set**.

Arithmetic operators are **not supported**.

---

## 5️⃣ Dictionary

Arithmetic operators **cannot be applied to dictionaries**.

Example:

```python
Dict1 = {1:100,2:"shyam",3:20.5}
Dict2 = {1:50,2:"Sahane",3:10.5}
```

All arithmetic operations will raise **TypeError**.

---

# 📊 Summary

| Data Type | Supported Operators |
|-----------|--------------------|
| Integer | All |
| Float | All |
| Boolean | All (except division by False) |
| String | + |
| Complex | + - * / |
| List | + |
| Tuple | + |
| Set | None |
| Frozenset | None |
| Dictionary | None |

---

# 🎯 Purpose of this Project

This code helps beginners understand:

- Python arithmetic operators
- How operators behave with different data types
- Which operations produce errors

It is useful for **Python beginners and interview preparation**.

---

# 👨‍💻 Author

**Harshal Warke**  
BCA Graduate  
Learning Python Programming