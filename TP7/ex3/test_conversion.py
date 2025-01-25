import unittest

from conversion import dollars_to_dirhams
from conversion import meters_to_kilometers

class Test_Conversion(unittest.TestCase):
    def dtd(self):
        self.assertEqual(dollars_to_dirhams(1),10)
        self.assertEqual(dollars_to_dirhams(0),0)
        self.assertEqual(dollars_to_dirhams(0.5),5)
    def mtk(self):
        self.assertEqual(meters_to_kilometers(1000),1)
        self.assertEqual(meters_to_kilometers(0),0)
        self.assertEqual(meters_to_kilometers(500),0.5)

if __name__ == "__main__":
    unittest.main()        