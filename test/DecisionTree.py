import unittest
from src import DecisionTree


class MyTestCase(unittest.TestCase):
    def test_fake_wrong(self):
     """   x = 12
        data = [12, 3, 1, 2, 4, 1, 5]
        w= DecisionTree.fake_title(data, x)
        self.assertEqual(w, 6)
       """

    def test_correct_worn(self):
     """   y = 12
        data = [12, 3, 1, 2, 4, 1, 5]
        w = DecisionTree.real_title(data, y)
        self.assertEqual(w, 0)
      """


if __name__ == '__main__':
    unittest.main()
