import unittest
from konbini.counter import Counter
from konbini.employee import Employee
from konbini.shelf import Shelf
from konbini.store import Store

class TestStore(unittest.TestCase):

    def test_new_store(self):
        store = Store('Store #1', 'Small Town ABC')
        self.assertIsNotNone(store.id)
        self.assertEqual(store.name, 'Store #1')
        self.assertEqual(store.location, 'Small Town ABC')
        self.assertEqual(store.money, Store.capital)
        self.assertEqual(store.currency, 'Gold')
        self.assertEqual(store.employees[0].name, 'Employee #1')
        self.assertEqual(store.displays[0].name, 'Shelf #1')
        self.assertEqual(store.displays[1].name, 'Counter #1')

    def test_details(self):
        store = Store('Store #1', 'Small Town ABC')
        result = store.details()
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'Store #1')
        self.assertEqual(result['location'], 'Small Town ABC')
        self.assertEqual(result['money'], Store.capital)
        self.assertEqual(result['currency'], 'Gold')
        self.assertEqual(result['employees'][0].name, 'Employee #1')
        self.assertEqual(result['displays'][0].name, 'Shelf #1')
        self.assertEqual(result['displays'][1].name, 'Counter #1')

    def test_add_shelf(self):
        store = Store('Store #1', 'Small Town ABC')
        details = store.details()
        self.assertEqual(len(details['displays']), 2)

        shelf = Shelf('Shelf #2', 'small')
        result = store.add_shelf(shelf)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])

        details = store.details()
        self.assertEqual(len(details['displays']), 3)
        self.assertEqual(details['displays'][2].name, 'Shelf #2')

    def test_add_counter(self):
        store = Store('Store #1', 'Small Town ABC')
        details = store.details()
        self.assertEqual(len(details['displays']), 2)

        counter = Counter('Counter #2')
        result = store.add_shelf(counter)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])

        details = store.details()
        self.assertEqual(len(details['displays']), 3)
        self.assertEqual(details['displays'][2].name, 'Counter #2')

    def test_add_employee(self):
        store = Store('Store #1', 'Small Town ABC')
        details = store.details()
        self.assertEqual(len(details['employees']), 1)

        employee = Employee('John Wick', 50000, 120, 100)
        result = store.add_employee(employee)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])

        details = store.details()
        self.assertEqual(len(details['employees']), 2)
        self.assertEqual(details['employees'][1].name, 'John Wick')

if __name__ == '__main__':
    unittest.main()
