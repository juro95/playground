

from abc import ABC, abstractmethod

#common interface
class IDescribable(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass

# Base Class
class Character(IDescribable):
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


# Interface Inheritance
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
class MagicalCreature( IDescribable):
    @abstractmethod
    def magical_ability(self) -> str:
        pass


class Dragon(MagicalCreature):
    def magical_ability(self) -> str:
        return "The dragon breathes fire."

    def describe(self) -> str:
        return "The dragon is lvl 6."


if __name__ == "__main__":
    print('------------------')
    character = Character("Aragorn", 5)
    print(character.describe())

    fighter = Fighter("Gimli", 6, "Two-Weapon Fighting")
    print(fighter.describe())

    wizard = Wizard("Gandalf", 10, "Evocation")
    print(wizard.describe())
    print(wizard.cast_spell("Fireball"))

    dragon = Dragon()
    print(dragon.magical_ability())
    print('------------------')

    #Polymorphism can be illustrated by creating a list of objects of different classes that share a common method.
    characters_and_creatures = [character, fighter, wizard, dragon]

    for entity in characters_and_creatures:
    
        print(entity.describe())
    print('------------------')


