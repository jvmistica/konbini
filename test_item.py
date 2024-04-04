import json
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
        result = json.loads(item.details())
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 20)
        self.assertEqual(result['price'], 1.99)
        self.assertFalse(result['counter'])

    def test_sell(self):
        item = Item('pudding', 20, 1.99, False)
        sell_result = item.sell(4)
        self.assertEqual(sell_result, 'pudding\'s count has decreased to 16')
        
        result = json.loads(item.details())
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 16)

    def test_restock(self):
        item = Item('pudding', 20, 1.99, False)
        restock_result = item.restock(30)
        self.assertEqual(restock_result, 'pudding\'s count has increased to 50')
        
        result = json.loads(item.details())
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 50)

    def test_update_price(self):
        item = Item('pudding', 20, 1.99, False)
        update_price_result = item.update_price(1.69)
        self.assertEqual(update_price_result, 'pudding\'s price is now 1.69')
        
        result = json.loads(item.details())
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['price'], 1.69)

    def test_remove(self):
        item = Item('pudding', 20, 1.99, False)
        remove_result = item.remove()
        self.assertEqual(remove_result, 'pudding has been removed from the inventory')
        
        result = json.loads(item.details())
        self.assertEqual(result['name'], 'pudding')
        self.assertEqual(result['count'], 0)

if __name__ == '__main__':
    unittest.main()
