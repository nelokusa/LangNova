# test_langnova.py
"""
Tests for LangNova module.
"""

import unittest
from langnova import LangNova

class TestLangNova(unittest.TestCase):
    """Test cases for LangNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LangNova()
        self.assertIsInstance(instance, LangNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LangNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
