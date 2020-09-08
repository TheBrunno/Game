class Couro:
    pass

class Helmet:
    tipe = 'helmet'

class Armor:
    tipe = 'armor'

class Legs:
    tipe = 'legs'

class Boots:
    tipe = 'boots'

class HelmetLeather(Helmet, Couro):
    name = 'Capacete De Couro'
    def __init__(self, ply):
        ply.defesa += 1

class ArmorLeather(Armor, Couro):
    name = 'Armadura De Couro'
    def __init__(self, ply):
        ply.defesa += 2

class LegsLeather(Legs, Couro):
    name = 'Calça De Couro'
    def __init__(self, ply):
        ply.defesa += 2

class BootsLeather(Boots, Couro):
    name = 'Bota De Couro'
    def __init__(self, ply):
        ply.defesa += 1