class Vocations:
    pass

class Druid(Vocations):
    def __init__(self, ply):
        ply.vida = 80
        ply.mana = 100
        ply.aumentoMana = 81
        ply.aumentoVida = 56

class Sorcerer(Vocations):
    def __init__(self, ply):
        ply.vida = 75
        ply.mana = 110
        ply.aumentoMana = 84
        ply.aumentoVida = 55

class Necromancer(Vocations):
    def __init__(self, ply):
        ply.vida = 75
        ply.mana = 120
        ply.aumentoMana = 75
        ply.aumentoVida = 51

class Paladin(Vocations):
    def __init__(self, ply):
        ply.vida = 90
        ply.mana = 90
        ply.aumentoMana = 61
        ply.aumentoVida = 69

class Archer(Vocations):
    def __init__(self, ply):
        ply.vida = 90
        ply.mana = 90
        ply.aumentoMana = 61
        ply.aumentoVida = 69

class Knight(Vocations):
    def __init__(self, ply):
        ply.vida = 140
        ply.mana = 50
        ply.aumentoMana = 45
        ply.aumentoVida = 84

class Berseker(Vocations):
    def __init__(self, ply):
        ply.vida = 150
        ply.mana = 40
        ply.aumentoMana = 40
        ply.aumentoVida = 90