import unittest
from counter import Counter
from item import Item
from employee import Employee
from helper import create_items

class TestCounter(unittest.TestCase):

    def test_new_counter(self):
        counter = Counter('Counter #1')
        self.assertEqual(counter.name, 'Counter #1')
        self.assertEqual(counter.slots, 8)

    def test_details(self):
        counter = Counter('Counter #1')
        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 8)
        self.assertEqual(len(result['items']), 0)

        item = Item('chocolate kariman', 20, 1.99, True)
        add_result = counter.add_item(item)
        self.assertFalse(add_result['error'])
        self.assertIsNone(add_result['error_message'])

        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate kariman')
        self.assertEqual(result['items'][0]['count'], 20)
        self.assertEqual(result['items'][0]['price'], 1.99)
        self.assertEqual(result['items'][0]['counter'], True)

    def test_remove(self):
        counter = Counter('Counter #1')
        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 8)
        self.assertEqual(result['status'], 'active')
        self.assertEqual(len(result['items']), 0)

        # valid removal
        remove_result = counter.remove()
        self.assertFalse(remove_result['error'])
        self.assertIsNone(remove_result['error_message'])
        self.assertEqual(counter.status, 'inactive')

        # invalid removal
        remove_result = counter.remove()
        self.assertTrue(remove_result['error'])
        self.assertEqual(remove_result['error_message'], 'Counter #1 is already inactive')
        self.assertEqual(counter.status, 'inactive')

    def test_assign_employee(self):
        counter = Counter('Counter #1')
        employee = Employee('Employee 1', 70000, 80, 100)

        # assign employee
        result = counter.assign_employee(employee)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        self.assertEqual(counter.employee, employee)

        # # unassign employee
        # result = counter.assign_employee('')
        # self.assertFalse(result['error'])
        # self.assertIsNone(result['error_message'])
        # self.assertEqual(counter.employee, '')

    def test_add_item(self):
        counter = Counter('Counter #1')
        items = create_items(9, True)

        for i, item in enumerate(items):
            result = counter.add_item(item)
            if i < 8:
                # valid addition
                self.assertFalse(result['error'])
                self.assertIsNone(result['error_message'])
            else:
                # invalid addition, no slots left
                self.assertTrue(result['error'])
                self.assertEqual(result['error_message'], 'Item cannot be added to Counter #1, all slots are taken')

        # invalid addition, not a counter item
        invalid_item = Item('Item 10', 30, 1.99, False)
        result = counter.add_item(invalid_item)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item 10 is not a type of item that can be added to Counter #1')

    def test_replace_item(self):
        counter = Counter('Counter #1')
        item = Item('chocolate kariman', 20, 1.99, True)
        add_result = counter.add_item(item)
        self.assertFalse(add_result['error'])
        self.assertIsNone(add_result['error_message'])
        
        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate kariman')

        # valid replace
        new_item = Item('dumplings', 25, 1.59, True)
        replace_result = counter.replace_item(item, new_item)
        self.assertFalse(replace_result['error'])
        self.assertIsNone(replace_result['error_message'])

        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'dumplings')

        # invalid replace, item being replaced does not exist
        new_item = Item('siopao', 25, 1.59, True)
        replace_result = counter.replace_item(item, new_item)
        self.assertTrue(replace_result['error'])
        self.assertEqual(replace_result['error_message'], 'Item \'chocolate kariman\' does not exist')

        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'dumplings')

    def test_remove_item(self):
        counter = Counter('Counter #1')
        item = Item('chocolate kariman', 20, 1.99, True)
        add_result = counter.add_item(item)
        self.assertFalse(add_result['error'])
        self.assertIsNone(add_result['error_message'])
        
        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate kariman')

        # valid removal
        remove_result = counter.remove_item(item)
        self.assertFalse(remove_result['error'])
        self.assertIsNone(remove_result['error_message'])
        
        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 8)
        self.assertEqual(len(result['items']), 0)

        # invalid removal
        remove_result = counter.remove_item(item)
        self.assertTrue(remove_result['error'])
        self.assertEqual(remove_result['error_message'], 'Item \'chocolate kariman\' does not exist')
        
        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 8)
        self.assertEqual(len(result['items']), 0)

if __name__ == '__main__':
    unittest.main()
