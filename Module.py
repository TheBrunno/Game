from random import randint

class Player:
    lvl = 1
    adv_lvl = 0
    vida = lvl * 100
    def ataque(self, arm, monster):
        monster.life -= arm.ataque
        if monster.life < 0:
            monster.life = 0
        return monster.life


class Mochila:
    def __init__(self):
        self.mochila = 'mochila.txt'
        try:
            mochila = open(self.mochila, 'r')
            mochila.close()
        except:
            mochila = open(self.mochila, 'w+')

    def Adicionar_mochila(self, item):
        with open(self.mochila, 'a') as mochila:
            mochila.write(item + '\n')

class Faca:
    ataque = randint(40, 60)

class Flecha:
    pass

class Arco:
    pass

class Orc:
    life = 100
    ataque = 20

class Minotauro:
    life = 150
    ataque = 30

