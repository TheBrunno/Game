from random import randint
from lib.Mochila import *


class Monsters:
    def Dropar(self, player):
        mochila = Mochila()
        for ele in range(len(self.drop)):
            ran = randint(0, 100)
            if ran <= self.porc[ele]:
                taxa = randint(1, self.qtd[ele])
                mochila.Adicionar_mochila(self.drop[ele], taxa)

    def atacarPlayer(self, player):
        player.vida -= self.ataque
        if player.vida <= 0:
            player.vida = 0
            if player.vivo:
                player.vivo = False
                return f'{player.nome_player} foi morto por {self.name}'
            else:
                return f'{player.nome_player} ja esta morto'
        return f'{self.name} ataca {player.nome_player} que ficou com {player.vida} de vida'



class Troll(Monsters):
    drop = ['Gold Coin', 'Troll Head', 'Meat']
    qtd = [5, 1, 4]
    porc = [50, 10, 40]
    name = 'Troll'
    life = 50
    ataque = randint(8, 12)
    exp = 15
    vivo = True


class Orc(Monsters):
    drop = ['Gold Coin', 'Orc Legs', 'Spear', 'Orc Hair']
    qtd = [8, 2, 4, 2]
    porc = [90, 15, 25, 27]
    name = 'Orc'
    life = 100
    ataque = randint(18, 22)
    exp = 30
    vivo = True


class Minotaur(Monsters):
    name = 'Minotaur'
    life = 150
    ataque = randint(28, 32)
    exp = 40
    vivo = True


class Skeleton(Monsters):
    name = 'Skeleton'
    life = 150
    ataque = randint(48, 52)
    exp = 45
    vivo = True


class Cursed_Skeleton(Monsters):
    name = 'Cursed Skeleton'
    life = 210
    ataque = randint(78, 82)
    exp = 105
    vivo = True

