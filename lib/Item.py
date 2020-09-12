from random import randint

class Life:
    tipe = 'Life'

class Mana:
    tipe = 'Mana'

class ManaPotion(Mana):
    Add = randint(70, 90)
    name = 'Mana Potion'

class LifePotion(Life):
    Add = randint(60, 80)
    name = 'Life Potion'

class Meat(Life):
    Add = randint(8, 12)
    name = 'Meat'