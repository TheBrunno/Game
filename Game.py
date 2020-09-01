from lib.Armas import Faquinha, Espada, ArcoSimples, FlechaSimples, Arcos, Flechas
from lib.Inimigos import Cursed_Skeleton, Troll, Orc, Monsters, Minotaur
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
listarminicial = ['Faquinha', 'Arco Simples (Vem com 25 flechas simples)']
name_player = leiaStr(' Digite o nome do player: ')
player = Player(f'{name_player}')
print(f'Seja bem vindo {name_player}...')
print('Vamos aprender alguns comandos basicos?')
print('Quer aprender a atacar monstros?\n')
op = Menu(listatu)
if op == 'Sim':
    troll = Minotaur()
    mochila = Mochila()
    if not mochila.VerificarItem('Faquinha') and not mochila.VerificarItem('Arco Simples'):
        arm = Menu(listarminicial)
        if arm == 'Faquinha' or arm[:12] == 'Arco Simples':
            if arm == 'Faquinha':
                arma = Faquinha()
            elif arm[:12] == 'Arco Simples':
                flecha = FlechaSimples()
                mochila.Adicionar_mochila(flecha.name, 25)
                arma = ArcoSimples(flecha)
            mochila.Adicionar_mochila(arma.name, 1)
            player.Equipar(arma)
    else:
        print('Qual arma usar?')
        sleep(1)
        lstArmas = mochila.MostrarArmas(False)
        armaEscolhida = Menu(lstArmas)
        player.Equipar(armaEscolhida)
    res = player.ModoAtaque(troll)
if op == 'Não':
    print('Ah, me parece que ja é experitente.. então vamos lá...')
sleep(1)
print('')
while True:
    troll0 = Minotaur()
    player.ModoAtaque(troll0)
