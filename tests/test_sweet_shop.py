import unittest
from src.sweet import Sweet
from src.shop import Shop

class TestSweetShop(unittest.TestCase):
    def test_add_sweet(self):
        shop = Shop()
        sweet = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50.0, quantity=20)
        shop.add_sweet(sweet)
        self.assertEqual(shop.get_sweet_by_id(1001), sweet)
        self.assertEqual(len(shop.sweets), 1)

    def test_add_sweet_duplicate_id(self):
        shop = Shop()
        sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50.0, quantity=20)
        shop.add_sweet(sweet1)
        sweet2 = Sweet(id=1001, name="Gulab Jamun", category="Milk-Based", price=10.0, quantity=50)
        with self.assertRaises(ValueError) as cm:
            shop.add_sweet(sweet2)
        self.assertEqual(str(cm.exception), "Sweet ID already exists")

    def test_delete_sweet(self):
        shop = Shop()
        sweet = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50.0, quantity=20)
        shop.add_sweet(sweet)
        shop.delete_sweet(1001)
        self.assertIsNone(shop.get_sweet_by_id(1001))
        self.assertEqual(len(shop.sweets), 0)

    def test_delete_nonexistent_sweet(self):
        shop = Shop()
        with self.assertRaises(ValueError) as cm:
            shop.delete_sweet(9999)
        self.assertEqual(str(cm.exception), "Sweet ID does not exist")

    # def test_sweet_initialization(self):
    #     sweet = Sweet(1, "Chocolate", "Candy", 2.5, 10)
    #     self.assertEqual(sweet.id, 1)
    #     self.assertEqual(sweet.name, "Chocolate")
    #     self.assertEqual(sweet.category, "Candy")
    #     self.assertEqual(sweet.price, 2.5)
    #     self.assertEqual(sweet.quantity, 10)

    # def test_sweet_with_invalid_id(self):
    #     with self.assertRaises(TypeError) as context:
    #         Sweet("one", "Chocolate", "Candy", 2.5, 10)
    #         self.assertEqual(str(context.exception), "ID must be an integer")

    # def test_negative_price(self):
    #     with self.assertRaises(ValueError) as context:
    #         Sweet(1, "Chocolate", "Candy", -2.5, 10)
    #         self.assertEqual(str(context.exception), "Price cannot be negative")

    # def test_negative_quantity(self):
    #     with self.assertRaises(ValueError) as context:
    #         Sweet(1, "Chocolate", "Candy", 2.5, -10)
    #         self.assertEqual(str(context.exception), "Quantity cannot be negative")
    
if __name__ == '__main__':
    unittest.main()