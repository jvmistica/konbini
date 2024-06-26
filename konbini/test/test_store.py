import unittest
from konbini.counter import Counter
from konbini.employee import Employee
from konbini.helper import create_items
from konbini.item import Item
from konbini.shelf import Shelf
from konbini.store import Store


class TestStore(unittest.TestCase):

    def setUp(self):
        self.store = Store('Store #1', 'Small Town ABC')

    def validate_initial_details(self, result: dict):
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'Store #1')
        self.assertEqual(result['location'], 'Small Town ABC')
        self.assertEqual(result['money'], Store.capital)
        self.assertEqual(result['currency'], 'Gold')
        self.assertEqual(result['employees'][0].name, 'Employee #1')
        self.assertEqual(result['displays'][0].name, 'Shelf #1')
        self.assertEqual(result['displays'][1].name, 'Counter #1')

    def validate_no_error(self, result: dict):
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])

    def test_details(self):
        result = self.store.details()
        self.validate_initial_details(result)

    def test_add_shelf(self):
        shelf = Shelf('Shelf #2', 'small')
        result = self.store.add_shelf(shelf)
        self.validate_no_error(result)

        details = self.store.details()
        self.assertEqual(len(details['displays']), 3)
        self.assertEqual(details['displays'][2].name, 'Shelf #2')
        self.assertEqual(details['money'], 95000)

    def test_add_counter(self):
        counter = Counter('Counter #2')
        result = self.store.add_counter(counter)
        self.validate_no_error(result)

        details = self.store.details()
        self.assertEqual(len(details['displays']), 3)
        self.assertEqual(details['displays'][2].name, 'Counter #2')
        self.assertEqual(details['money'], 93500)

    def test_add_employee(self):
        employee = Employee('John Wick', 50000, 120, 100)
        result = self.store.add_employee(employee)
        self.validate_no_error(result)

        details = self.store.details()
        self.assertEqual(len(details['employees']), 2)
        self.assertEqual(details['employees'][1].name, 'John Wick')

    def test_add_item_shelf(self):
        shelf = Shelf('Shelf #1', 'small')
        result = self.store.add_shelf(shelf)
        self.validate_no_error(result)

        cost = shelf.cost
        items = create_items(5, False)
        for i, item in enumerate(items):
            result = self.store.add_item(shelf, item)
            if i < shelf.sizes['small']:
                # valid addition
                cost += (item.count * item.price)
                self.validate_no_error(result)
                self.assertAlmostEqual(self.store.money, Store.capital - cost)
                self.assertEqual(self.store.displays[2].name, 'Shelf #1')
                self.assertEqual(len(self.store.displays[2].items), i + 1)
            else:
                # invalid addition, no slots left
                self.assertTrue(result['error'])
                self.assertEqual(result['error_message'], 'Item cannot be added to Shelf #1, all slots are taken')
                self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # invalid addition, not a shelf item
        invalid_item = Item('Item 5', 30, 1.99, True)
        result = self.store.add_item(shelf, invalid_item)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item 5 is not a type of item that can be added to Shelf #1')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

    def test_add_item_counter(self):
        counter = Counter('Counter #1')
        result = self.store.add_counter(counter)
        self.validate_no_error(result)

        cost = counter.cost
        items = create_items(8, True)
        for i, item in enumerate(items):
            result = self.store.add_item(counter, item)
            if i < 8:
                # valid addition
                cost += (item.count * item.price)
                self.validate_no_error(result)
                self.assertAlmostEqual(self.store.money, Store.capital - cost)
                self.assertEqual(self.store.displays[2].name, 'Counter #1')
                self.assertEqual(len(self.store.displays[2].items), i + 1)
            else:
                 # invalid addition, no slots left
                 self.assertTrue(result['error'])
                 self.assertEqual(result['error_message'], 'Item cannot be added to Counter #1, all slots are taken')
                 self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # invalid addition, not a counter item
        invalid_item = Item('Item 5', 30, 1.99, False)
        result = self.store.add_item(counter, invalid_item)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item 5 is not a type of item that can be added to Counter #1')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

    def test_replace_item_shelf(self):
        shelf = Shelf('Shelf #1', 'small')
        result = self.store.add_shelf(shelf)
        self.validate_no_error(result)

        item = Item('pudding', 20, 1.99, False)
        cost = shelf.cost + (item.count * item.price)
        result = self.store.add_item(shelf, item)
        self.validate_no_error(result)
        
        self.assertEqual(self.store.displays[2].name, 'Shelf #1')
        self.assertEqual(self.store.displays[2].slots, 3)
        self.assertEqual(len(self.store.displays[2].items), 1)
        self.assertEqual(self.store.displays[2].items[0].name, 'pudding')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # valid replace
        new_item = Item('chocolate', 25, 1.59, False)
        cost += new_item.count * new_item.price
        result = self.store.replace_item(shelf, item, new_item)
        self.validate_no_error(result)

        self.assertEqual(self.store.displays[2].slots, 3)
        self.assertEqual(len(self.store.displays[2].items), 1)
        self.assertEqual(self.store.displays[2].items[0].name, 'chocolate')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # invalid replace, item does not exist
        new_item = Item('cake', 25, 1.59, False)
        result = self.store.replace_item(shelf, item, new_item)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item \'pudding\' does not exist')

        self.assertEqual(self.store.displays[2].slots, 3)
        self.assertEqual(len(self.store.displays[2].items), 1)
        self.assertEqual(self.store.displays[2].items[0].name, 'chocolate')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

    def test_replace_item_counter(self):
        counter = Counter('Counter #1')
        result = self.store.add_counter(counter)
        self.validate_no_error(result)

        item = Item('kariman', 20, 1.99, True)
        cost = counter.cost + (item.count * item.price)
        result = self.store.add_item(counter, item)
        self.validate_no_error(result)
        
        self.assertEqual(self.store.displays[2].name, 'Counter #1')
        self.assertEqual(self.store.displays[2].slots, 7)
        self.assertEqual(len(self.store.displays[2].items), 1)
        self.assertEqual(self.store.displays[2].items[0].name, 'kariman')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # valid replace
        new_item = Item('siopao', 25, 1.59, True)
        cost += new_item.count * new_item.price
        result = self.store.replace_item(counter, item, new_item)
        self.validate_no_error(result)

        self.assertEqual(self.store.displays[2].slots, 7)
        self.assertEqual(len(self.store.displays[2].items), 1)
        self.assertEqual(self.store.displays[2].items[0].name, 'siopao')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # invalid replace, item does not exist
        new_item = Item('dumplings', 25, 1.59, True)
        result = self.store.replace_item(counter, item, new_item)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item \'kariman\' does not exist')

        self.assertEqual(self.store.displays[2].slots, 7)
        self.assertEqual(len(self.store.displays[2].items), 1)
        self.assertEqual(self.store.displays[2].items[0].name, 'siopao')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

    def test_remove_item_shelf(self):
        shelf = Shelf('Shelf #1', 'small')
        result = self.store.add_shelf(shelf)
        self.validate_no_error(result)

        item = Item('pudding', 20, 1.99, False)
        cost = shelf.cost + (item.count * item.price)
        result = self.store.add_item(shelf, item)
        self.validate_no_error(result)
        
        self.assertEqual(self.store.displays[2].name, 'Shelf #1')
        self.assertEqual(self.store.displays[2].slots, 3)
        self.assertEqual(len(self.store.displays[2].items), 1)
        self.assertEqual(self.store.displays[2].items[0].name, 'pudding')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # valid removal
        result = self.store.remove_item(shelf, item)
        self.validate_no_error(result)
        self.assertEqual(self.store.displays[2].slots, 4)
        self.assertEqual(len(self.store.displays[2].items), 0)
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # invalid removal
        result = self.store.remove_item(shelf, item)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item \'pudding\' does not exist')
        
        self.assertEqual(self.store.displays[2].slots, 4)
        self.assertEqual(len(self.store.displays[2].items), 0)
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

    def test_remove_item_counter(self):
        counter = Counter('Counter #1')
        result = self.store.add_counter(counter)
        self.validate_no_error(result)

        item = Item('kariman', 20, 1.99, True)
        cost = counter.cost + (item.count * item.price)
        result = self.store.add_item(counter, item)
        self.validate_no_error(result)
        
        self.assertEqual(self.store.displays[2].name, 'Counter #1')
        self.assertEqual(self.store.displays[2].slots, 7)
        self.assertEqual(len(self.store.displays[2].items), 1)
        self.assertEqual(self.store.displays[2].items[0].name, 'kariman')
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # valid removal
        result = self.store.remove_item(counter, item)
        self.validate_no_error(result)
        self.assertEqual(self.store.displays[2].slots, 8)
        self.assertEqual(len(self.store.displays[2].items), 0)
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

        # invalid removal
        result = self.store.remove_item(counter, item)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item \'kariman\' does not exist')
        
        self.assertEqual(self.store.displays[2].slots, 8)
        self.assertEqual(len(self.store.displays[2].items), 0)
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

    def test_restock_item_counter(self):
        counter = Counter('Counter #1')
        result = self.store.add_counter(counter)
        self.validate_no_error(result)

        item = Item('kariman', 20, 1.99, True)
        cost = counter.cost + (item.count * item.price)
        result = self.store.add_item(counter, item)
        self.validate_no_error(result)

        result = item.restock(30)
        self.validate_no_error(result)
        self.assertEqual(self.store.displays[2].name, 'Counter #1')
        self.assertEqual(self.store.displays[2].items[0].name, 'kariman')
        self.assertEqual(self.store.displays[2].items[0].count, 50)
        self.assertAlmostEqual(self.store.money, Store.capital - cost)

    def test_sell_item_shelf(self):
        shelf = Shelf('Shelf #1', 'small')
        result = self.store.add_shelf(shelf)
        self.validate_no_error(result)

        item = Item('ramen', 20, 1.99, False)
        cost = shelf.cost + (item.count * item.price)
        result = self.store.add_item(shelf, item)
        self.validate_no_error(result)

        # valid
        result = self.store.sell_item(shelf, item, 2)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])

        # invalid count
        result = self.store.sell_item(shelf, item, 25)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Cannot sell 25 amount of items, remaining stock is 18')

        # invalid item
        new_item = Item('candy', 20, 1.50, False)
        result = self.store.sell_item(shelf, new_item, 2)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item \'candy\' does not exist in \'Shelf #1\'')

    def test_sell_item_counter(self):
        counter = Counter('Counter #1')
        result = self.store.add_counter(counter)
        self.validate_no_error(result)

        item = Item('kariman', 20, 1.99, True)
        cost = counter.cost + (item.count * item.price)
        result = self.store.add_item(counter, item)
        self.validate_no_error(result)

        # valid
        result = self.store.sell_item(counter, item, 2)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])

        # invalid count
        result = self.store.sell_item(counter, item, 25)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Cannot sell 25 amount of items, remaining stock is 18')

        # invalid item
        new_item = Item('siopao', 20, 1.50, True)
        result = self.store.sell_item(counter, new_item, 2)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item \'siopao\' does not exist in \'Counter #1\'')


if __name__ == '__main__':
    unittest.main()
