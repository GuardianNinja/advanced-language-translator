# Advanced Language Translator

A phonetic mapping system for translating symbolic language tokens into their phonetic representations.

## Features

- **Phonetic Mapping**: Translates symbolic tokens to phonetic sounds
- **Flexible Translation**: Unknown tokens are preserved in the output
- **Simple API**: Easy-to-use `chant()` function

## Phonetic Mappings

| Symbol | Phonetic Sound |
|--------|----------------|
| spiral | flao |
| triangle_eye | si |
| dot_cluster | spir |
| arc_wave | flo |
| heart | luv |
| mandala | balan |
| tear | wep |

## Usage

```python
from translator import phonetic_map, chant

# Translate a list of tokens
result = chant(["spiral", "heart"])
print(result)  # Output: "flao luv"

# Multiple tokens
result = chant(["triangle_eye", "dot_cluster", "arc_wave"])
print(result)  # Output: "si spir flo"

# Unknown tokens are kept as-is
result = chant(["mandala", "unknown", "tear"])
print(result)  # Output: "balan unknown wep"
```

## Running Examples

```bash
python example.py
```

## Running Tests

```bash
python -m unittest test_translator.py -v
```
