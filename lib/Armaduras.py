class Armadura:
    pass

class Helmet:
    tipe = 'helmet'

class Armor:
    tipe = 'armor'

class Legs:
    tipe = 'legs'

class Boots:
    tipe = 'boots'

class HelmetLeather(Helmet, Armadura):
    name = 'Capacete De Couro'
    def __init__(self, ply):
        ply.defesa += 1

class ArmorLeather(Armor, Armadura):
    name = 'Armadura De Couro'
    def __init__(self, ply):
        ply.defesa += 2

class LegsLeather(Legs, Armadura):
    name = 'Calça De Couro'
    def __init__(self, ply):
        ply.defesa += 2

class BootsLeather(Boots, Armadura):
    name = 'Bota De Couro'
    def __init__(self, ply):
        ply.defesa += 1