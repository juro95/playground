

from abc import ABC, abstractmethod

# Base Class
class Character:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def describe(self) -> str:
        return f"{self.name} is a level {self.level} character."


# Single Inheritance
class Fighter(Character):
    def __init__(self, name: str, level: int, fighting_style: str):
        super().__init__(name, level)
        self.fighting_style = fighting_style

    def describe(self) -> str:
        return f"{self.name} is a level {self.level} Fighter with {self.fighting_style} fighting style."


# Interface Inheritance
# this class serves as a blueprint for other classes to inherit from 
# and implement the cast_spell method, otherwise they will not be able to instantiate.
# interfaces should only contain abstract methods
class ICastSpells(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str) -> str:
        pass

# Multiple Inheritance
class Wizard(Character, ICastSpells):
    def __init__(self, name: str, level: int, spell_school: str):
        super().__init__(name, level)
        self.spell_school = spell_school

    def cast_spell(self, spell_name: str) -> str:
        return f"{self.name} casts {spell_name} from the school of {self.spell_school}."
    

# Abstract Class
class MagicalCreature(ABC):
    @abstractmethod
    def magical_ability(self) -> str:
        pass
    
    # concrete method that can be used by all subclasses but does not have to be implemented
    def describe(self) -> str:
        return f"A {self.name} is a magical creature."


class Dragon(MagicalCreature):
    def __init__(self):
        self.name = "Dragon"

    def magical_ability(self) -> str:
        return f"{self.name} breathes fire."  
    



if __name__ == "__main__":
    character = Character("Aragorn", 5)
    print(character.describe())

    fighter = Fighter("Gimli", 6, "Two-Weapon Fighting")
    print(fighter.describe())

    wizard = Wizard("Gandalf", 10, "Evocation")
    print(wizard.describe())
    print(wizard.cast_spell("Fireball"))
    print(wizard.describe())
    dragon = Dragon()
    print(dragon.magical_ability())
