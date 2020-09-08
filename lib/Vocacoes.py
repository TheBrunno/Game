class Druid:
    def __init__(self, ply):
        ply.tipe_voc = 'druid'
        ply.vida_initial = 80
        ply.mana_initial = 100
        ply.vida = 80
        ply.mana = 100
        ply.aumentoMana = 81
        ply.aumentoVida = 56
        ply.defesa = 5

class Sorcerer:
    def __init__(self, ply):
        ply.tipe_voc = 'sorcerer'
        ply.vida_initial = 75
        ply.mana_initial = 110
        ply.vida = 75
        ply.mana = 110
        ply.aumentoMana = 84
        ply.aumentoVida = 55
        ply.defesa = 5

class Necromancer:
    def __init__(self, ply):
        ply.tipe_voc = 'necromancer'
        ply.vida_initial = 75
        ply.mana_initial = 120
        ply.vida = 75
        ply.mana = 120
        ply.aumentoMana = 75
        ply.aumentoVida = 51
        ply.defesa = 5

class Paladin:
    def __init__(self, ply):
        ply.tipe_voc = 'paladin'
        ply.vida_initial = 90
        ply.mana_initial = 90
        ply.vida = 90
        ply.mana = 90
        ply.aumentoMana = 61
        ply.aumentoVida = 69
        ply.defesa = 10

class Archer:
    def __init__(self, ply):
        ply.tipe_voc = 'archer'
        ply.vida_initial = 90
        ply.mana_initial = 90
        ply.vida = 90
        ply.mana = 90
        ply.aumentoMana = 61
        ply.aumentoVida = 69
        ply.defesa = 10

class Knight:
    def __init__(self, ply):
        ply.tipe_voc = 'knight'
        ply.vida_initial = 140
        ply.mana_initial = 50
        ply.vida = 140
        ply.mana = 50
        ply.aumentoMana = 45
        ply.aumentoVida = 84
        ply.defesa = 15

class Berseker:
    def __init__(self, ply):
        ply.tipe_voc = 'berseker'
        ply.vida_initial = 150
        ply.mana_initial = 40
        ply.vida = 150
        ply.mana = 40
        ply.aumentoMana = 40
        ply.aumentoVida = 90
        ply.defesa = 18