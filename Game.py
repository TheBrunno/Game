from lib.Armas import Faquinha, Espada
from lib.Inimigos import Cursed_Skeleton, Troll, Orc, Monsters
from lib.Mochila import Mochila
from lib.Player import Player
from lib.Item import LifePotion



def Menu(lst):
    print('-=' * 10)
    for ind, ele in enumerate(lst):
        print(f'{ind + 1} - {ele}')
    print('-=' * 10)



listaAtk = ['Atacar monstro']
faca = Espada()
# name_player = input('Digite o nome do player: ')
player = Player('name_player')
# print(f'Seja bem vindo {name_player}...')
# print('Vamos aprender alguns comandos basicos? Vamos nessa:')
troll = Orc()
print(troll.atacarPlayer(player))
print(troll.atacarPlayer(player))
print(troll.atacarPlayer(player))
print(troll.atacarPlayer(player))
pot = LifePotion()
player.Usar(pot)
print(player.vida)