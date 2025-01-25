import unittest
from ..src import add,sous,multi,div

class test_math_operations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(1, 0.5), 1.5)
    def test_soustraction(self):
        self.assertEqual(sous(2, 1), 1)
        self.assertEqual(sous(1, -2), 3)
        self.assertEqual(sous(1, 0.5), 0.5)
    def test_multiplication(self):
        self.assertEqual(multi(1, 2), 2)
        self.assertEqual(multi(1, -2), -2)
        self.assertEqual(multi(1, 0.5), 0.5)
    def test_division(self):
        self.assertEqual(div(1, 2) , 0.5)
        self.assertEqual(div(1, -2), -0.5)
        self.assertEqual(div(1, 0.5), 0.5)

if __name__ == "__main__":
    unittest.main()
        