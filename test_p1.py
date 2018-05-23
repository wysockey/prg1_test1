import unittest 
from p1 import is_square

class TestCases(unittest.TestCase):
	"""Tests for `final exam.py`."""
	def test_is_square_positives(self):
		"""is_square => testing values that are squares"""
		self.assertTrue(is_square(1))
		self.assertTrue(is_square(4))
		self.assertTrue(is_square(16))
		self.assertTrue(is_square(100))
		for x in range(100,900):
			self.assertTrue(is_square(x*x))

	def test_is_square_negatives(self):
		"""is_square => test values that are not squares"""
		self.assertFalse(is_square(3))
		self.assertFalse(is_square(6))
		for x in range(24965,25279):
			self.assertFalse(is_square(x))

	def test_is_square_negative_numbers(self):
		"""is_square => test values that are squares but are negative numbers"""
		for x in range(-100,0):
			self.assertFalse(is_square(x))
			
			

			
if __name__ == '__main__':
    unittest.main()
						