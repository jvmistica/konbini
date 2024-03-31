import json
import unittest
from counter import Counter
from item import Item
from employee import Employee
from helper import create_items

# TODO:
# setup and teardown methods
# break down and clean-up tests
class TestCounter(unittest.TestCase):

    def test_new_counter(self):
        counter = Counter('Counter #1')
        self.assertEqual(counter.name, 'Counter #1')
        self.assertEqual(counter.slots, 8)

    def test_details(self):
        counter = Counter('Counter #1')
        result = json.loads(counter.details())
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 8)
        self.assertEqual(len(result['items']), 0)

        item = Item('chocolate kariman', 20, 1.99, True)
        add_result = counter.add_item(item)
        self.assertEqual(add_result, 'Item has been added to the counter')

        result = json.loads(counter.details())
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate kariman')
        self.assertEqual(result['items'][0]['count'], 20)
        self.assertEqual(result['items'][0]['price'], 1.99)
        self.assertEqual(result['items'][0]['counter'], True)

    def test_remove(self):
        counter = Counter('Counter #1')
        result = json.loads(counter.details())
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 8)
        self.assertEqual(result['status'], 'active')
        self.assertEqual(len(result['items']), 0)

        remove_result = counter.remove()
        self.assertEqual(remove_result, 'Counter #1 has been removed from the display')
        self.assertEqual(counter.status, 'inactive')

    def test_assign_employee(self):
        # assign employee
        counter = Counter('Counter #1')
        employee = Employee('Employee 1', 70000, 80, 100)
        result = counter.assign_employee(employee)
        self.assertEqual(counter.employee, employee)
        self.assertEqual(result, 'Employee 1 has been assigned to counter Counter #1')

        # unassign employee
        result = counter.assign_employee('')
        self.assertEqual(counter.employee, '')
        self.assertEqual(result, 'Counter Counter #1 has no employee assigned')

    def test_add_item(self):
        counter = Counter('Counter #1')
        items = create_items(9, True)

        for i, item in enumerate(items):
            result = counter.add_item(item)
            if i < 8:
                # valid
                self.assertEqual(result, 'Item has been added to the counter')
            else:
                # no slots left
                self.assertEqual(result, 'Item cannot be added to the counter, all slots are taken')

        # not a counter item
        invalid_item = Item('Item 10', 30, 1.99, False)
        result = counter.add_item(invalid_item)
        self.assertEqual(result, 'Item 10 is not a type of item that can be added to a counter')

    def test_replace_item(self):
        counter = Counter('Counter #1')
        item = Item('chocolate kariman', 20, 1.99, True)
        add_result = counter.add_item(item)
        self.assertEqual(add_result, 'Item has been added to the counter')
        
        result = json.loads(counter.details())
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate kariman')

        # valid replace
        new_item = Item('dumplings', 25, 1.59, True)
        replace_result = counter.replace_item(item, new_item)
        self.assertEqual(replace_result, f'Discarded: {item.name}\nAdded: {new_item.name}')

        result = json.loads(counter.details())
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'dumplings')

        # invalid replace: item being replaced does not exist
        new_item = Item('siopao', 25, 1.59, True)
        with self.assertRaises(ValueError):
            counter.replace_item(item, new_item)

        result = json.loads(counter.details())
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'dumplings')

    def test_remove_item(self):
        counter = Counter('Counter #1')
        item = Item('chocolate kariman', 20, 1.99, True)
        add_result = counter.add_item(item)
        self.assertEqual(add_result, 'Item has been added to the counter')
        
        result = json.loads(counter.details())
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate kariman')

        remove_result = counter.remove_item(item)
        self.assertEqual(remove_result, 'Item "chocolate kariman" has been removed from the counter')
        
        result = json.loads(counter.details())
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 8)
        self.assertEqual(len(result['items']), 0)

if __name__ == '__main__':
    unittest.main()
