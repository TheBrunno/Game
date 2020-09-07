from random import randint
from lib.Mochila import Mochila


class Monsters:
    def __init__(self):
        print(f'O monstro \'{self.name}\' apareceu com {self.life} de HP')

    def Dropar(self, player):
        mochila = Mochila()
        for ele in range(len(self.drop)):
            ran = randint(0, 100)
            if ran <= self.porc[ele]:
                taxa = randint(1, self.qtd[ele])
                mochila.Adicionar_mochila(self.drop[ele], taxa)

    def atacarPlayer(self, player):
        player.vida -= int(self.ataque - (self.ataque * player.defesa / 100))
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
    porc = [60, 7, 40]
    name = 'Troll'
    life = 50
    ataque = randint(15, 30)
    exp = 15
    vivo = True
    conversavel = True
    msgNot = 'Troll não entendeu muito bem oque você disse'
    msgTru = 'Troll não entendeu oque disse, mas acha que você não é uma ameaça'


class Orc(Monsters):
    drop = ['Gold Coin', 'Orc Legs', 'Spear', 'Orc Hair', 'Orelha de Orc']
    qtd = [8, 2, 4, 2, 1]
    porc = [90, 15, 25, 27, 2]
    name = 'Orc'
    life = 150
    ataque = randint(14, 27)
    exp = 30
    vivo = True
    conversavel = True
    msgNot = 'Orc não terá piedade de você...'
    msgTru = 'As orelhas de Orc estão coçando... ele deixa você ir para coça-la'


class Minotaur(Monsters):
    drop = ['Gold Coin', 'Mace', 'Minotaur Skin', 'Book']
    qtd = [16, 1, 2, 1]
    porc = [70, 5, 18, 8]
    name = 'Minotaur'
    life = 210
    ataque = randint(15, 30)
    exp = 70
    vivo = True
    conversavel = False
    msgNot = 'Minotaur lutará bravamente até derramar seu sangue'


class Skeleton(Monsters):
    drop = ['Gold Coin', 'Bone', 'Skull', 'Flask of the death']
    qtd = [28, 3, 2, 1]
    porc = [80, 56, 18, 2]
    name = 'Skeleton'
    life = 320
    ataque = randint(48, 52)
    exp = 45
    vivo = True
    conversavel = True
    msgNot = 'Skeleton não gosta muito de vivos, por isso ele ira te matar para ser seu amigo :D...'
    msgTru = 'Skeleton vê que você não será um amigo tão legal e te deixa ir...'




class Cursed_Skeleton(Monsters):
    drop = ['Gold Coin', 'Cursed Bone', 'Cursed Skull', 'Flask of the death', 'Bone Ascent']
    qtd = [35, 2, 1, 3, 1]
    porc = [80, 56, 15, 7, 1]
    name = 'Cursed Skeleton'
    life = 415
    ataque = randint(78, 82)
    exp = 105
    vivo = True
    conversavel = False
    msgNot = 'Cursed Skeleton se enche de ódio e nunca te deixará sair'

