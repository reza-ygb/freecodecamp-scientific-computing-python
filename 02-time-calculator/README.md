# Time Calculator

## 📝 Project Description

This is the second project in the FreeCodeCamp "Scientific Computing with Python" certification. The Time Calculator adds time durations and calculates start and end times for different days of the week.

## ✨ Features

- **Time Addition**: Add duration to a start time
- **Day Calculation**: Calculate what day it will be after adding time
- **Multiple Day Support**: Handle time spans across multiple days
- **12-hour Format**: Works with AM/PM time format
- **Flexible Input**: Accepts various time and duration formats

## 🎯 Requirements

The function should add a duration time to a start time and return the result. If the result will be the next day, it should show `(next day)`. If the result will be more than one day later, it should show `(n days later)` where n is the number of days later.

The function should also optionally take a starting day of the week as a third parameter. In this case, the output should display the day of the week of the result, in addition to the time.

### Example Usage

**Basic Time Addition:**
```python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32")
# Returns: 2:02 PM
```

**With Day Transition:**
```python
add_time("11:43 PM", "24:20")
# Returns: 12:03 AM (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

**With Starting Day:**
```python
add_time("3:00 PM", "3:10", "Monday")
# Returns: 6:10 PM, Monday

add_time("2:59 AM", "24:00", "saturDay")
# Returns: 2:59 AM, Sunday (next day)
```

## 🚀 Implementation Details

The solution handles:

1. **Time Parsing**: Converting time strings to workable format
2. **Duration Addition**: Adding hours and minutes properly
3. **Day Calculation**: Determining day changes and day of week
4. **Format Conversion**: Converting back to 12-hour format
5. **Edge Cases**: Handling midnight, multiple days, etc.

## 🧪 Testing

To test the time calculator:

```python
from main import add_time

# Test basic functionality
result = add_time("3:00 PM", "3:10")
print(result)  # Expected: 6:10 PM

# Test with day parameter
result = add_time("3:00 PM", "3:10", "Monday")
print(result)  # Expected: 6:10 PM, Monday
```

## 📚 What I Learned

- Time manipulation and calculation in Python
- Working with modular arithmetic for time conversion
- String parsing and formatting
- Handling edge cases in time calculations
- Day of week calculations

---

**Part of:** [FreeCodeCamp Scientific Computing with Python Certification](../README.md)
