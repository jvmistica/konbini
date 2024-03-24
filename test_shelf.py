import unittest
from shelf import Shelf
from item import Item

class TestShelf(unittest.TestCase):

    def test_add(self):
        shelf = Shelf('Shelf #1', 4)
        item1 = Item('pudding', 20, 1.99)
        item2 = Item('ramen', 50, 0.99)
        item3 = Item('soda', 40, 1.50)
        item4 = Item('chocolate', 50, 1.99)
        item5 = Item('cake', 20, 2.30)

        result = shelf.add(item1)
        self.assertEqual(result, 'Item has been added to the shelf')

        result = shelf.add(item2)
        self.assertEqual(result, 'Item has been added to the shelf')

        result = shelf.add(item3)
        self.assertEqual(result, 'Item has been added to the shelf')

        result = shelf.add(item4)
        self.assertEqual(result, 'Item has been added to the shelf')

        result = shelf.add(item5)
        self.assertEqual(result, 'Item cannot be added to the shelf, all slots are taken.')

        details = shelf.details()
        items = [{'name': 'pudding', 'count': 20, 'price': 1.99},
                 {'name': 'ramen', 'count': 50, 'price': 0.99},
                 {'name': 'soda', 'count': 40, 'price': 1.5},
                 {'name': 'chocolate', 'count': 50, 'price': 1.99}]
        self.assertEqual(details, f'Name: Shelf #1\nSlots: 0\nItems: {items}')

    def test_details(self):
        shelf = Shelf('Shelf #1', 4)
        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 4\nItems: []')

        item = Item('pudding', 20, 1.99)
        add_result = shelf.add(item)
        result = shelf.details()
        self.assertEqual(add_result, 'Item has been added to the shelf')
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 3\nItems: [{\'name\': \'pudding\', \'count\': 20, \'price\': 1.99}]')

    def test_remove(self):
        shelf = Shelf('Shelf #1', 4)
        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 4\nItems: []')
        self.assertEqual(shelf.status, 'Active')

        remove_result = shelf.remove()
        self.assertEqual(remove_result, 'Shelf #1 has been removed from the display')
        self.assertEqual(shelf.status, 'Inactive')

if __name__ == '__main__':
    unittest.main()
