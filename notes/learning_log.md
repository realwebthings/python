# Python Learning Log

## Session 1 - Environment Setup
**Date:** $(date +%Y-%m-%d)

### What I Learned:
- How to create a Python virtual environment
- Importance of isolating project dependencies
- Basic virtual environment commands

### Commands Used:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Key Concepts:
- **Virtual Environment**: Isolated Python environment for project dependencies
- **Activation**: Makes the virtual environment active for current terminal session

### Next Steps:
- Learn Python basics
- Start with variables and data types

---

## Session 2 - Variables and Debugging
**Date:** $(date +%Y-%m-%d)

### What I Learned:
- Python variables and string concatenation
- VSCode debugger setup and execution
- Virtual environment integration with debugging

### Code Created:
```python
name = "Aman"
print("Hello, " + name + "!")
```

### Key Concepts:
- **Variables**: Store data values (`name = "Aman"`)
- **String Concatenation**: Joining strings with `+`
- **Debugging**: Running code with VSCode debugger

### Debugging Verified:
- ✅ Virtual environment active
- ✅ Debugger working correctly
- ✅ Output displaying in terminal

---

## Session 3 - String Methods
**Date:** $(date +%Y-%m-%d)

### What I Learned:
- String manipulation methods (upper, lower, replace, split)
- String validation methods (startswith, endswith, isalpha, isnumeric)
- String slicing with positive and negative indices
- Slice objects and their usage
- Code readability best practices

### Key Concepts:
- **String Methods**: Built-in functions for string manipulation
- **Slicing**: Extracting parts of strings using [start:end:step]
- **Negative Indexing**: Counting from the end of string
- **Code Quality**: Importance of readable and maintainable code

### Issues Fixed:
- ✅ Invalid slice bounds (slice(6, -11) → slice(6, 11))
- ✅ Complex chained method calls → separate variable
- ✅ Added proper comments and explanations

---

*This log will be updated after each learning session*