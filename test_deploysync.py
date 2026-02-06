# test_deploysync.py
"""
Tests for deploySync module.
"""

import unittest
from deploysync import deploySync

class TestdeploySync(unittest.TestCase):
    """Test cases for deploySync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = deploySync()
        self.assertIsInstance(instance, deploySync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = deploySync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
