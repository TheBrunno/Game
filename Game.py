from lib.Armas import Faquinha, Espada
from lib.Inimigos import Cursed_Skeleton, Troll, Orc, Monsters
from lib.Mochila import Mochila
from lib.Player import Player, Menu, LeiaInt
from lib.Item import LifePotion, ManaPotion


listatu = ['Sim', 'Não']
name_player = input('Digite o nome do player: ').title()
player = Player(f'{name_player}')
print(f'Seja bem vindo {name_player}...')
print('Vamos aprender alguns comandos basicos?\n')
print('Quer aprender a atacar monstros?')
faca = Faquinha
troll = Troll()
player.ModoAtaque(faca, troll)
