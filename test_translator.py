import unittest
from io import StringIO
import sys
from translator import archive_seal


class TestArchiveSeal(unittest.TestCase):
    def test_archive_seal_output(self):
        """Test that archive_seal produces the correct output format"""
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the function
        archive_seal("TestName", "test purpose")
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        expected = "Seal of TestName 1.0 — marking test purpose.\n"
        self.assertEqual(captured_output.getvalue(), expected)
    
    def test_archive_seal_different_values(self):
        """Test archive_seal with different input values"""
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the function
        archive_seal("Project", "completion")
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        expected = "Seal of Project 1.0 — marking completion.\n"
        self.assertEqual(captured_output.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
