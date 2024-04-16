import uuid
from konbini.item import Item


class Display:

    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.active = True
        self.items = []

    def remove(self) -> dict:
        """
        Removes a display.
        """

        if self.active == False:
            return {
                'error': True,
                'error_message': f'{self.name} is already inactive'
            }

        self.active = False
        return {
            'error': False,
            'error_message': None
        }
