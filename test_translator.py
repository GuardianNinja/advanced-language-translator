import unittest
from io import StringIO
from contextlib import redirect_stdout
from translator import archive_seal


class TestArchiveSeal(unittest.TestCase):
    def _capture_output(self, name, meaning):
        """Helper method to capture stdout from archive_seal"""
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            archive_seal(name, meaning)
        return captured_output.getvalue()
    
    def test_archive_seal_output(self):
        """Test that archive_seal produces the correct output format"""
        output = self._capture_output("TestName", "test purpose")
        expected = "Seal of TestName 1.0 — marking test purpose.\n"
        self.assertEqual(output, expected)
    
    def test_archive_seal_different_values(self):
        """Test archive_seal with different input values"""
        output = self._capture_output("Project", "completion")
        expected = "Seal of Project 1.0 — marking completion.\n"
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
