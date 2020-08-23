from lib.Armas import Faquinha, Espada, ArcoSimples, FlechaSimples, Arcos, Flechas
from lib.Inimigos import Cursed_Skeleton, Troll, Orc, Monsters
from lib.Mochila import Mochila
from lib.Player import Player, Menu, LeiaInt
from lib.Item import LifePotion, ManaPotion
from time import sleep

def dinamicPrint(msg, car='-'):
    print(car[0] * (len(msg) + 4))
    print(f'  {msg}')
    print(car[0] * (len(msg) + 4))

def leiaStr(msg):
    while True:
        passou = False
        name_player = input(msg).title()
        for num, let in enumerate(name_player):
            if let.isnumeric():
                dinamicPrint('NÃO É PERMITIDO NÚMEROS, Digite um nome valido')
                break
            else:
                if num + 1 == len(name_player):
                    passou = True
        if passou:
            if num + 1 == len(name_player):
                return name_player


listatu = ['Sim', 'Não']
name_player = leiaStr(' Digite o nome do player: ')
player = Player(f'{name_player}')
print(f'Seja bem vindo {name_player}...')
print('Vamos aprender alguns comandos basicos?')
print('Quer aprender a atacar monstros?\n')
op = Menu(listatu)
sleep(2)
if op == 1:
    flecha = FlechaSimples()
    faca = ArcoSimples(flecha)
    troll = Troll()
    player.ModoAtaque(faca, troll)
if op == 2:
    print('Ah, me parece que ja é experitente.. então vamos lá...')
sleep(1)
print('')
