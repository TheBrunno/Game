class Druid:
    def __init__(self, ply):
        ply.tipe_voc = 'druid'
        ply.vida_initial = 50
        ply.mana_initial = 80
        ply.vida = 50
        ply.mana = 80
        ply.aumentoMana = 58
        ply.aumentoVida = 28
        ply.defesa = 5

class Sorcerer:
    def __init__(self, ply):
        ply.tipe_voc = 'sorcerer'
        ply.vida_initial = 45
        ply.mana_initial = 85
        ply.vida = 45
        ply.mana = 85
        ply.aumentoMana = 60
        ply.aumentoVida = 26
        ply.defesa = 5

class Necromancer:
    def __init__(self, ply):
        ply.tipe_voc = 'necromancer'
        ply.vida_initial = 30
        ply.mana_initial = 100
        ply.vida = 30
        ply.mana = 100
        ply.aumentoMana = 65
        ply.aumentoVida = 21
        ply.defesa = 5

class Paladin:
    def __init__(self, ply):
        ply.tipe_voc = 'paladin'
        ply.vida_initial = 60
        ply.mana_initial = 70
        ply.vida = 65
        ply.mana = 65
        ply.aumentoMana = 45
        ply.aumentoVida = 41
        ply.defesa = 10

class Archer:
    def __init__(self, ply):
        ply.tipe_voc = 'archer'
        ply.vida_initial = 70
        ply.mana_initial = 60
        ply.vida = 70
        ply.mana = 70
        ply.aumentoMana = 41
        ply.aumentoVida = 45
        ply.defesa = 11

class Knight:
    def __init__(self, ply):
        ply.tipe_voc = 'knight'
        ply.vida_initial = 100
        ply.mana_initial = 30
        ply.vida = 100
        ply.mana = 30
        ply.aumentoMana = 22
        ply.aumentoVida = 64
        ply.defesa = 15

class Berseker:
    def __init__(self, ply):
        ply.tipe_voc = 'berseker'
        ply.vida_initial = 110
        ply.mana_initial = 20
        ply.vida = 110
        ply.mana = 20
        ply.aumentoMana = 14
        ply.aumentoVida = 72
        ply.defesa = 18