# 📊 Pandas Data Analysis Examples

This repository contains **Python scripts** with commented examples for beginners learning about data structures, operators, functions, and the Pandas library.  

The goal is to provide **didactic code** that can be copied, executed, and modified in order to understand how Python works for **data analysis**.

---

## 📁 Files

### 1. `lists-tuples-sets-operators.py`
This file introduces Python **built-in data structures** and basic operators:

- **Lists (`list`)** → ordered and mutable collections.
- **Tuples (`tuple`)** → ordered and immutable collections.
- **Sets (`set`)** → unordered collections, no duplicates.
- **FrozenSets (`frozenset`)** → immutable sets.
- **Operators** → comparison (`==`, `!=`, `<`, `>`), logical (`and`, `or`, `not`), and arithmetic (`+`, `-`, `*`, `/`, `%`, `**`).

👉 This script shows how to create, modify, and use these structures in real scenarios.

---

### 2. `complex-numbers-functions.py`
This file explains:

- **Complex numbers** in Python  
  - Written as `a + bj` (where `a` is the real part and `bj` the imaginary part).  
  - Useful in **engineering, physics, mathematics, and signal processing**.  
  - Example: `(2 + 3j) * (1 - 4j) = (14 - 5j)`  

- **Functions in Python**  
  - How to define reusable blocks of code.  
  - Functions with **parameters** and with **default values**.  
  - Example:  
    ```python
    def potencia(base, expoente=2):
        return base ** expoente
    ```
    - `potencia(3)` → 9 (default exponent 2)  
    - `potencia(2, 5)` → 32  

---

### 3. `pandas-dataframe.py`
This file introduces the **Pandas** library, one of the most important tools for data analysis.

Covered topics:
- Creating DataFrames from dictionaries and lists.
- Accessing columns and filtering rows.
- Concatenating DataFrames.
- Practical examples such as filtering by salary or combining tables.

Example:
```python
df[df["Salário"] > 4000]
