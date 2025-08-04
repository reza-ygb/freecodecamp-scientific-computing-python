# Arithmetic Formatter

## 📝 Project Description

This is the first project in the FreeCodeCamp "Scientific Computing with Python" certification. The Arithmetic Formatter arranges arithmetic problems vertically and side by side to make them easier to read and solve.

## ✨ Features

- **Vertical Arrangement**: Formats math problems in a vertical layout
- **Input Validation**: Comprehensive error checking for invalid inputs
- **Optional Answers**: Can display the calculated answers below each problem
- **Clean Formatting**: Properly aligned output with consistent spacing

## 🎯 Requirements

The function should arrange the arithmetic problems vertically and side by side. The function should take a list of strings that are arithmetic problems and return the problems arranged vertically and side by side.

### Input Validation

The function should return an error for the following scenarios:
- If there are **too many problems** supplied to the function (more than 5)
- If the **operator is not '+' or '-'**
- If the **numbers contain non-digits**
- If **numbers are more than 4 digits**

### Example

**Function Call:**
```python
arithmetic_arranger(['34 + 658', '285 - 49', '254 + 18', '542 - 412'])
```

**Output:**
```
   34      285      254      542
+ 658    -  49    +  18    - 412
-----    -----    -----    -----
```

**With Answers:**
```python
arithmetic_arranger(['34 + 658', '285 - 49', '254 + 18', '542 - 412'], True)
```

**Output:**
```
   34      285      254      542
+ 658    -  49    +  18    - 412
-----    -----    -----    -----
  692      236      272      130
```

## 🚀 Usage

```python
from main import arithmetic_arranger

# Basic usage without answers
result = arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49'])
print(result)

# With answers displayed
result = arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49'], True)
print(result)

# Error handling examples
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
# Output: Error: Numbers cannot be more than four digits.

print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
# Output: Error: Numbers must only contain digits.
```

## 🧪 Testing

To run the basic tests:

```bash
python main.py
```

## 🔧 Implementation Details

The solution uses several key concepts:

1. **String Manipulation**: Using `.split()` to parse problems and `.rjust()` for alignment
2. **Input Validation**: Multiple checks for different error conditions
3. **String Formatting**: Building output strings with proper spacing and alignment
4. **Conditional Logic**: Handling optional answer display

## 📚 What I Learned

- String manipulation and formatting in Python
- Input validation and error handling
- Working with loops and conditional statements
- Code organization and documentation
- Problem decomposition and algorithmic thinking

---

**Part of:** [FreeCodeCamp Scientific Computing with Python Certification](../README.md)
