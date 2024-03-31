import json
import unittest
from shelf import Shelf
from item import Item
from helper import create_items

# TODO:
# setup and teardown methods
# break down and clean-up tests
class TestShelf(unittest.TestCase):

    def test_new_shelf(self):
        # small shelf
        shelf = Shelf('Shelf #1', 'small')
        self.assertEqual(shelf.name, 'Shelf #1')
        self.assertEqual(shelf.slots, 4)
        self.assertEqual(shelf.size, 'small')

        # medium shelf
        shelf = Shelf('Shelf #1', 'medium')
        self.assertEqual(shelf.name, 'Shelf #1')
        self.assertEqual(shelf.slots, 8)
        self.assertEqual(shelf.size, 'medium')

        # medium shelf
        shelf = Shelf('Shelf #1', 'large')
        self.assertEqual(shelf.name, 'Shelf #1')
        self.assertEqual(shelf.slots, 12)
        self.assertEqual(shelf.size, 'large')

        # invalid size shelf
        with self.assertRaises(ValueError):
            Shelf('Shelf #2', 'extra-large')

    def test_details(self):
        shelf = Shelf('Shelf #1', 'small')
        result = json.loads(shelf.details())
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 4)
        self.assertEqual(len(result['items']), 0)

        item = Item('pudding', 20, 1.99, False)
        add_result = shelf.add_item(item)
        self.assertEqual(add_result, 'Item has been added to the shelf')

        result = json.loads(shelf.details())
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'pudding')
        self.assertEqual(result['items'][0]['count'], 20)
        self.assertEqual(result['items'][0]['price'], 1.99)
        self.assertEqual(result['items'][0]['counter'], False)

    def test_remove(self):
        shelf = Shelf('Shelf #1', 'small')
        result = json.loads(shelf.details())
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['status'], 'active')

        remove_result = shelf.remove()
        self.assertEqual(remove_result, 'Shelf #1 has been removed from the display')
        self.assertEqual(shelf.status, 'inactive')

    def test_add_item(self):
        shelf = Shelf('Shelf #1', 'small')

        items = create_items(5, False)
        for i, item in enumerate(items):
            result = shelf.add_item(item)
            if i < 4:
                # valid
                self.assertEqual(result, 'Item has been added to the shelf')
            else:
                # no slots left
                self.assertEqual(result, 'Item cannot be added to the shelf, all slots are taken')

        # not a shelf item
        invalid_item = Item('Item 5', 30, 1.99, True)
        result = shelf.add_item(invalid_item)
        self.assertEqual(result, 'Item 5 is not a type of item that can be added to a shelf')

    def test_replace_item(self):
        shelf = Shelf('Shelf #1', 'small')
        item = Item('pudding', 20, 1.99, False)
        add_result = shelf.add_item(item)
        self.assertEqual(add_result, 'Item has been added to the shelf')
        
        result = json.loads(shelf.details())
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'pudding')

        # valid replace
        new_item = Item('chocolate', 25, 1.59, False)
        replace_result = shelf.replace_item(item, new_item)
        self.assertEqual(replace_result, f'Discarded: {item.name}\nAdded: {new_item.name}')

        result = json.loads(shelf.details())
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate')

        # invalid replace: item being replaced does not exist
        new_item = Item('cake', 25, 1.59, False)
        with self.assertRaises(ValueError):
            shelf.replace_item(item, new_item)

        result = json.loads(shelf.details())
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate')

    def test_remove_item(self):
        shelf = Shelf('Shelf #1', 'small')
        item = Item('pudding', 20, 1.99, False)
        add_result = shelf.add_item(item)
        self.assertEqual(add_result, 'Item has been added to the shelf')
        
        result = json.loads(shelf.details())
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(result['items'][0]['name'], 'pudding')

        remove_result = shelf.remove_item(item)
        self.assertEqual(remove_result, 'Item "pudding" has been removed from the shelf')
        
        result = json.loads(shelf.details())
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 4)
        self.assertEqual(len(result['items']), 0)

if __name__ == '__main__':
    unittest.main()
