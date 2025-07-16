import unittest
from src.sweet import Sweet

class TestSweetShop(unittest.TestCase):
    def test_sweet_initialization(self):
        sweet = Sweet(1, "Chocolate", "Candy", 2.5, 10)
        self.assertEqual(sweet.id, 1)
        self.assertEqual(sweet.name, "Chocolate")
        self.assertEqual(sweet.category, "Candy")
        self.assertEqual(sweet.price, 2.5)
        self.assertEqual(sweet.quantity, 10)

if __name__ == '__main__':
    unittest.main()