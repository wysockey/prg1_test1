import unittest
from ec import is_happy

class TestCases(unittest.TestCase):
	"""Tests for `final exam.py`."""
	def test_is_happy_positive(self):
		self.assertTrue(is_happy(130))
		self.assertTrue(is_happy(133))
		self.assertTrue(is_happy(139))
		self.assertTrue(is_happy(167))
		self.assertTrue(is_happy(176))
	def test_is_happy_negative(self):
		self.assertFalse(is_happy(5))
		self.assertFalse(is_happy(11))
		self.assertFalse(is_happy(45))

		
if __name__ == '__main__':
	unittest.main()

