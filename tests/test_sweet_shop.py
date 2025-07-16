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

    def test_sweet_with_invalid_id(self):
        with self.assertRaises(TypeError) as context:
            Sweet("one", "Chocolate", "Candy", 2.5, 10)
            self.assertEqual(str(context.exception), "ID must be an integer")
            
    def test_negative_price(self):
        with self.assertRaises(ValueError) as context:
            Sweet(1, "Chocolate", "Candy", -2.5, 10)
            self.assertEqual(str(context.exception), "Price cannot be negative")

    def test_negative_quantity(self):
        with self.assertRaises(ValueError) as context:
            Sweet(1, "Chocolate", "Candy", 2.5, -10)
            self.assertEqual(str(context.exception), "Quantity cannot be negative")
    
if __name__ == '__main__':
    unittest.main()