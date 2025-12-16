# advanced-language-translator
new translator adaptor

## NaytrunesInterpreter

A stack-based interpreter for the Naytrunes language.

### Features

The NaytrunesInterpreter implements a simple stack-based language with the following operations:

- **spiral**: Replicates the top value on the stack (duplicates it)
- **triangle_eye**: Prints and pops the top value from the stack
- **heart**: Assigns the top value from the stack to variable "A"
- **Any other token**: Pushes the token onto the stack

### Usage

```python
from naytrunes_interpreter import NaytrunesInterpreter

# Create an interpreter instance
interpreter = NaytrunesInterpreter()

# Execute a program
interpreter.execute([5, "spiral", "triangle_eye"])
# Output: 5
# Stack: [5]

# Access variables
interpreter.execute([42, "heart"])
# Variables: {"A": 42}
```

### Running Tests

```bash
python -m unittest test_naytrunes_interpreter.py -v
```

### Example

Run the example script to see the interpreter in action:

```bash
python example_usage.py
```
