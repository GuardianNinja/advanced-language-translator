import unittest
from io import StringIO
import sys
from naytrunes_interpreter import NaytrunesInterpreter


class TestNaytrunesInterpreter(unittest.TestCase):
    
    def setUp(self):
        self.interpreter = NaytrunesInterpreter()
    
    def test_init(self):
        """Test that the interpreter initializes with empty stack and vars"""
        self.assertEqual(self.interpreter.stack, [])
        self.assertEqual(self.interpreter.vars, {})
    
    def test_push_values(self):
        """Test pushing values onto the stack"""
        self.interpreter.execute([1, 2, 3])
        self.assertEqual(self.interpreter.stack, [1, 2, 3])
    
    def test_spiral_replicate(self):
        """Test spiral command replicates top of stack"""
        self.interpreter.execute([5, "spiral"])
        self.assertEqual(self.interpreter.stack, [5, 5])
    
    def test_spiral_empty_stack(self):
        """Test spiral on empty stack does nothing"""
        self.interpreter.execute(["spiral"])
        self.assertEqual(self.interpreter.stack, [])
    
    def test_triangle_eye_print(self):
        """Test triangle_eye prints and pops from stack"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.interpreter.execute([42, "triangle_eye"])
        
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "42")
        self.assertEqual(self.interpreter.stack, [])
    
    def test_triangle_eye_empty_stack(self):
        """Test triangle_eye on empty stack does nothing"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.interpreter.execute(["triangle_eye"])
        
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "")
        self.assertEqual(self.interpreter.stack, [])
    
    def test_heart_assign(self):
        """Test heart assigns top of stack to variable A"""
        self.interpreter.execute([100, "heart"])
        self.assertEqual(self.interpreter.vars, {"A": 100})
        self.assertEqual(self.interpreter.stack, [])
    
    def test_heart_empty_stack(self):
        """Test heart on empty stack does nothing"""
        self.interpreter.execute(["heart"])
        self.assertEqual(self.interpreter.vars, {})
        self.assertEqual(self.interpreter.stack, [])
    
    def test_complex_program(self):
        """Test a complex program with multiple operations"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Push 10, replicate it, assign one to A, print the other
        self.interpreter.execute([10, "spiral", "heart", "triangle_eye"])
        
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "10")
        self.assertEqual(self.interpreter.vars, {"A": 10})
        self.assertEqual(self.interpreter.stack, [])
    
    def test_mixed_types(self):
        """Test with different types of values"""
        self.interpreter.execute(["hello", 42, 3.14])
        self.assertEqual(self.interpreter.stack, ["hello", 42, 3.14])
    
    def test_sequential_operations(self):
        """Test multiple operations in sequence"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.interpreter.execute([1, 2, 3, "spiral", "triangle_eye", "triangle_eye"])
        
        sys.stdout = sys.__stdout__
        output_lines = captured_output.getvalue().strip().split('\n')
        self.assertEqual(output_lines, ["3", "3"])
        self.assertEqual(self.interpreter.stack, [1, 2])


if __name__ == "__main__":
    unittest.main()
