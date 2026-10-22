# error class
class CharacterDefeatedError(Exception):
    def __init__(self, character):
        super().__init__(f"{character.name} has already been defeated!")

class NotEnoughManaError(Exception):
    def __init__(self, character):
        super().__init__(f"{character.name} does not have enough mana to use {character.power_name}!")

class NotEnoughArrowsError(Exception):
    def __init__(self, character):
        super().__init__(f"{character} does not have enough arrows!")
