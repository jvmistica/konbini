import unittest
from item import Item

class TestItem(unittest.TestCase):

    def test_new_item(self):
        item = Item('pudding', 20, 1.99, False)
        self.assertIsNotNone(item.id)
        self.assertEqual(item.name, 'pudding')
        self.assertEqual(item.count, 20)
        self.assertEqual(item.price, 1.99)
        self.assertFalse(item.counter)

    def test_details(self):
        item = Item('pudding', 20, 1.99, False)
        result = item.details()
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 20)
        self.assertEqual(result['price'], 1.99)
        self.assertFalse(result['counter'])

    def test_sell(self):
        item = Item('pudding', 20, 1.99, False)

        # stock available
        sell_result = item.sell(4)
        self.assertFalse(sell_result['error'])
        self.assertIsNone(sell_result['error_message'])
        
        result = item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 16)
        
        # stock unavailable
        sell_result = item.sell(17)
        self.assertTrue(sell_result['error'])
        self.assertEqual(sell_result['error_message'], 'Cannot sell 17 amount of items, remaining stock: 16')
        
        result = item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 16)

    def test_restock(self):
        item = Item('pudding', 20, 1.99, False)

        # valid re-stock value
        restock_result = item.restock(30)
        self.assertFalse(restock_result['error'])
        self.assertIsNone(restock_result['error_message'])
        
        result = item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 50)

        # invalid re-stock value
        restock_result = item.restock(15)
        self.assertTrue(restock_result['error'])
        self.assertEqual(restock_result['error_message'], 'Cannot re-stock 15 amount of items, minimum re-stock value: 20')
        
        result = item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 50)

    def test_update_price(self):
        item = Item('pudding', 20, 1.99, False)
        update_price_result = item.update_price(1.69)
        self.assertFalse(update_price_result['error'])
        self.assertIsNone(update_price_result['error_message'])
        
        result = item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['price'], 1.69)

    def test_remove(self):
        item = Item('pudding', 20, 1.99, False)

        # valid removal
        remove_result = item.remove()
        self.assertFalse(remove_result['error'])
        self.assertIsNone(remove_result['error_message'])
        
        result = item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 0)

        # invalid removal
        remove_result = item.remove()
        self.assertTrue(remove_result['error'])
        self.assertEqual(remove_result['error_message'], 'Cannot remove item, amount is already zero')
        
        result = item.details()
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 0)

if __name__ == '__main__':
    unittest.main()
