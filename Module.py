from random import randint

class Player:
    lvl = 1
    vida = lvl * 100
    def __init__(self, nome):
        self.nome_player = nome
        self.exp_player = 0

    def ataque(self, arm, monster):
        monster.life -= arm.ataque
        exp = 0
        if monster.life <= 0:
            monster.life = 0
            if monster.vivo:
                monster.vivo = False
                exp += monster.exp
                return f'{self.nome_player} matou {monster.name}.\n{self.nome_player} ganhou {exp} de exp'
            else:
                return f'{monster.name} ja esta morto'
        else:
            return f'{self.nome_player} atacou {monster.name} que ficou com {monster.life} de vida'

        


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
    vivo = True
    exp = 30
    name = 'Orc'
    life = 100
    ataque = 20

class Minotauro:
    vivo = True
    exp = 40
    name = 'Minotauro'
    life = 150
    ataque = 30

