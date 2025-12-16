"""
Tests for the Advanced Language Translator phonetic mapping system.
"""

import unittest
from translator import phonetic_map, chant


class TestPhoneticMap(unittest.TestCase):
    """Test cases for the phonetic mapping functionality."""
    
    def test_phonetic_map_exists(self):
        """Test that phonetic_map dictionary is properly defined."""
        self.assertIsInstance(phonetic_map, dict)
        self.assertEqual(len(phonetic_map), 7)
    
    def test_phonetic_map_values(self):
        """Test that phonetic_map contains the correct mappings."""
        expected_mappings = {
            "spiral": "flao",
            "triangle_eye": "si",
            "dot_cluster": "spir",
            "arc_wave": "flo",
            "heart": "luv",
            "mandala": "balan",
            "tear": "wep"
        }
        self.assertEqual(phonetic_map, expected_mappings)
    
    def test_chant_single_token(self):
        """Test chant function with a single token."""
        result = chant(["spiral"])
        self.assertEqual(result, "flao")
        
        result = chant(["heart"])
        self.assertEqual(result, "luv")
    
    def test_chant_multiple_tokens(self):
        """Test chant function with multiple tokens."""
        result = chant(["spiral", "heart"])
        self.assertEqual(result, "flao luv")
        
        result = chant(["triangle_eye", "dot_cluster", "arc_wave"])
        self.assertEqual(result, "si spir flo")
    
    def test_chant_all_tokens(self):
        """Test chant function with all available tokens."""
        tokens = ["spiral", "triangle_eye", "dot_cluster", "arc_wave", "heart", "mandala", "tear"]
        result = chant(tokens)
        self.assertEqual(result, "flao si spir flo luv balan wep")
    
    def test_chant_unknown_token(self):
        """Test chant function with tokens not in the phonetic_map."""
        result = chant(["unknown"])
        self.assertEqual(result, "unknown")
        
        result = chant(["spiral", "unknown", "heart"])
        self.assertEqual(result, "flao unknown luv")
    
    def test_chant_empty_list(self):
        """Test chant function with an empty list."""
        result = chant([])
        self.assertEqual(result, "")
    
    def test_chant_mixed_known_unknown(self):
        """Test chant function with a mix of known and unknown tokens."""
        result = chant(["spiral", "xyz", "heart", "abc"])
        self.assertEqual(result, "flao xyz luv abc")


if __name__ == "__main__":
    unittest.main()
