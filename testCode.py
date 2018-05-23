import unittest
from main import is_square
from main import is_factorion
from main import is_happy

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

    def test_is_factorion_positive(self):
	"""is_square => test values that should be factorions"""
	self.assertTrue(is_factorion(1))
	self.assertTrue(is_factorion(2))
	self.assertTrue(is_factorion(145))
	self.assertTrue(is_factorion(40585))

    def test_is_factorion_negative(self):
	"""is_factorion => test values that should not be factorions"""
	for x in range(40585, 42585):
		self.assertFalse(is_factorion(40585))

    def test_is_happy_positive(self):
	self.assertTrue(130)
	self.assertTrue(133)
	self.assertTrue(139)
	self.assertTrue(167)
	self.assertTrue(176)
    def test_is_happy_negative(self):
	self.assertFalse(5)
	self.assertFalse(11)
	self.assertFalse(45)


if __name__ == '__main__':
    unittest.main()

