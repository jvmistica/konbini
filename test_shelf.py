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
        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 4\nItems: []')

        item = Item('pudding', 20, 1.99, False)
        add_result = shelf.add_item(item)
        result = shelf.details()
        self.assertEqual(add_result, 'Item has been added to the shelf')
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 3\nItems: [{\'name\': \'pudding\', \'count\': 20, \'price\': 1.99}]')

    def test_remove(self):
        shelf = Shelf('Shelf #1', 'small')
        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 4\nItems: []')
        self.assertEqual(shelf.status, 'Active')

        remove_result = shelf.remove()
        self.assertEqual(remove_result, 'Shelf #1 has been removed from the display')
        self.assertEqual(shelf.status, 'Inactive')

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
        
        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 3\nItems: [{\'name\': \'pudding\', \'count\': 20, \'price\': 1.99}]')

        # valid replace
        new_item = Item('chocolate', 25, 1.59, False)
        replace_result = shelf.replace_item(item, new_item)
        self.assertEqual(replace_result, f'Discarded: {item.name}\nAdded: {new_item.name}')

        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 3\nItems: [{\'name\': \'chocolate\', \'count\': 25, \'price\': 1.59}]')

        # invalid replace: item being replaced does not exist
        new_item = Item('cake', 25, 1.59, False)
        with self.assertRaises(ValueError):
            shelf.replace_item(item, new_item)

        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 3\nItems: [{\'name\': \'chocolate\', \'count\': 25, \'price\': 1.59}]')

    def test_remove_item(self):
        shelf = Shelf('Shelf #1', 'small')
        item = Item('pudding', 20, 1.99, False)
        add_result = shelf.add_item(item)
        self.assertEqual(add_result, 'Item has been added to the shelf')
        
        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 3\nItems: [{\'name\': \'pudding\', \'count\': 20, \'price\': 1.99}]')

        remove_result = shelf.remove_item(item)
        self.assertEqual(remove_result, 'Item "pudding" has been removed from the shelf')
        
        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 4\nItems: []')

if __name__ == '__main__':
    unittest.main()
