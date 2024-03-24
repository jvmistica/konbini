import unittest
from shelf import Shelf
from item import Item

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

    def test_add_item(self):
        shelf = Shelf('Shelf #1', 'small')
        item1 = Item('pudding', 20, 1.99, False)
        item2 = Item('ramen', 50, 0.99, False)
        item3 = Item('soda', 40, 1.50, False)
        item4 = Item('chocolate', 50, 1.99, False)
        item5 = Item('cake', 20, 2.30, False)

        result = shelf.add_item(item1)
        self.assertEqual(result, 'Item has been added to the shelf')

        result = shelf.add_item(item2)
        self.assertEqual(result, 'Item has been added to the shelf')

        result = shelf.add_item(item3)
        self.assertEqual(result, 'Item has been added to the shelf')

        result = shelf.add_item(item4)
        self.assertEqual(result, 'Item has been added to the shelf')

        result = shelf.add_item(item5)
        self.assertEqual(result, 'Item cannot be added to the shelf, all slots are taken')

        details = shelf.details()
        items = [{'name': 'pudding', 'count': 20, 'price': 1.99},
                 {'name': 'ramen', 'count': 50, 'price': 0.99},
                 {'name': 'soda', 'count': 40, 'price': 1.5},
                 {'name': 'chocolate', 'count': 50, 'price': 1.99}]
        self.assertEqual(details, f'Name: Shelf #1\nSlots: 0\nItems: {items}')

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

    def test_replace(self):
        shelf = Shelf('Shelf #1', 'small')
        item = Item('pudding', 20, 1.99, False)
        add_result = shelf.add_item(item)
        self.assertEqual(add_result, 'Item has been added to the shelf')
        
        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 3\nItems: [{\'name\': \'pudding\', \'count\': 20, \'price\': 1.99}]')

        # valid replace
        new_item = Item('chocolate', 25, 1.59, False)
        replace_result = shelf.replace(item, new_item)
        self.assertEqual(replace_result, f'Discarded: {item.name}\nAdded: {new_item.name}')

        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 3\nItems: [{\'name\': \'chocolate\', \'count\': 25, \'price\': 1.59}]')

        # invalid replace
        new_item = Item('cake', 25, 1.59, False)
        with self.assertRaises(ValueError):
            shelf.replace(item, new_item)

        result = shelf.details()
        self.assertEqual(result, 'Name: Shelf #1\nSlots: 3\nItems: [{\'name\': \'chocolate\', \'count\': 25, \'price\': 1.59}]')

if __name__ == '__main__':
    unittest.main()
