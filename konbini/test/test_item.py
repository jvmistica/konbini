import unittest
from konbini.item import Item


class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item('pudding', 20, 1.99, False)

    def tearDown(self):
        self.item.remove()

    def validate_initial_details(self, result: dict):
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 20)
        self.assertEqual(result['price'], 1.99)
        self.assertEqual(result['retail_price'], 1.99 * 1.05)
        self.assertFalse(result['counter'])

    def test_new_item(self):
        item = Item('pudding', 20, 1.99, False)
        self.assertIsNotNone(item.id)
        self.assertEqual(item.name, 'pudding')
        self.assertEqual(item.count, 20)
        self.assertEqual(item.price, 1.99)
        self.assertFalse(item.counter)

    def test_details(self):
        result = self.item.details()
        self.validate_initial_details(result)

    def test_sell(self):
        result = self.item.details()
        self.validate_initial_details(result)

        # stock available
        result = self.item.sell(4)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        
        result = self.item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 16)
        
        # stock unavailable
        result = self.item.sell(17)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Cannot sell 17 amount of items, remaining stock: 16')
        
        result = self.item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 16)

    def test_restock(self):
        result = self.item.details()
        self.validate_initial_details(result)

        # valid re-stock value
        result = self.item.restock(30)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        
        result = self.item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 50)

        # invalid re-stock value
        result = self.item.restock(15)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Cannot re-stock 15 amount of items, minimum re-stock value: 20')
        
        result = self.item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 50)

    def test_update_price(self):
        result = self.item.details()
        self.validate_initial_details(result)

        result = self.item.update_price(1.69)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        
        result = self.item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['price'], 1.69)

    def test_remove(self):
        result = self.item.details()
        self.validate_initial_details(result)

        # valid removal
        result = self.item.remove()
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        
        result = self.item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 0)

        # invalid removal
        result = self.item.remove()
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Cannot remove item, amount is already zero')
        
        result = self.item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 0)


if __name__ == '__main__':
    unittest.main()
