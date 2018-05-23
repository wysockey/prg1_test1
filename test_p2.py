import unittest
from p2 import is_factorion

class TestCases(unittest.TestCase):
	"""Tests for `final exam.py`."""
	def test_is_factorion_positive(self):
		"""is_square => test values that should be factorions"""
		self.assertTrue(is_factorion(1))
		self.assertTrue(is_factorion(2))
		self.assertTrue(is_factorion(145))
		self.assertTrue(is_factorion(40585))

	def test_is_factorion_negative(self):
		"""is_factorion => test values that should not be factorions"""
		for x in range(40586, 42583):
			self.assertFalse(is_factorion(x)) 
			

			
if __name__ == '__main__':
    unittest.main()
			