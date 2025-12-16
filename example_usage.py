#!/usr/bin/env python3
"""
Example usage of the NaytrunesInterpreter class.

This script demonstrates the basic operations:
- spiral: replicates the top value on the stack
- triangle_eye: prints and pops the top value from the stack
- heart: assigns the top value to variable A
- any other token: pushes the token onto the stack
"""

from naytrunes_interpreter import NaytrunesInterpreter


def main():
    # Create an interpreter instance
    interpreter = NaytrunesInterpreter()
    
    print("Example 1: Basic stack operations")
    print("Tokens: [5, 'spiral', 'triangle_eye']")
    interpreter.execute([5, "spiral", "triangle_eye"])
    print(f"Stack after: {interpreter.stack}")
    print(f"Variables: {interpreter.vars}\n")
    
    # Reset for next example
    interpreter = NaytrunesInterpreter()
    
    print("Example 2: Variable assignment")
    print("Tokens: [42, 'heart']")
    interpreter.execute([42, "heart"])
    print(f"Stack after: {interpreter.stack}")
    print(f"Variables: {interpreter.vars}\n")
    
    # Reset for next example
    interpreter = NaytrunesInterpreter()
    
    print("Example 3: Complex program")
    print("Tokens: [10, 20, 'spiral', 'heart', 'triangle_eye', 'triangle_eye']")
    interpreter.execute([10, 20, "spiral", "heart", "triangle_eye", "triangle_eye"])
    print(f"Stack after: {interpreter.stack}")
    print(f"Variables: {interpreter.vars}\n")
    
    # Reset for next example
    interpreter = NaytrunesInterpreter()
    
    print("Example 4: String values")
    print("Tokens: ['hello', 'spiral', 'triangle_eye']")
    interpreter.execute(["hello", "spiral", "triangle_eye"])
    print(f"Stack after: {interpreter.stack}")
    print(f"Variables: {interpreter.vars}")


if __name__ == "__main__":
    main()
