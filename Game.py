from lib.Armas import Faquinha, Espada, ArcoSimples, FlechaSimples, Arcos, Flechas
from lib.Inimigos import Cursed_Skeleton, Troll, Orc, Monsters, Minotaur
from lib.Mochila import Mochila
from lib.Player import Player, Menu, LeiaInt
from lib.Item import LifePotion, ManaPotion
from lib.Vocacoes import Druid, Archer, Berseker, Knight, Necromancer, Sorcerer, Paladin
from lib.Armaduras import HelmetLeather
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

time = 0
# print('Bruno: Olá Aventureiro! Me parece que é novo por aqui não é mesmo?\n')
# sleep(time)
# print('Bruno: Meu nome é Bruno, eu estou preso neste mundo a algum tempo. Conheço bastente sobre,\nE eu te guiarei \"até conseguir andar com suas próprias pernas\" :D \n')
# sleep(time)
while True:
    name_player = leiaStr(' Bruno: Poderia me dizer seu nome: ').strip()
    if name_player != 'Bruno':
        break
    print('\nESCOLHA OUTRO NOME\n')
player = Player(f'{name_player}')
if player.voc == None:
    print('\nOk, antes de começar você precisa escolher sua vocação, (ESCOLHA COM CUIDADO, DEPOIS NÃO SERÁ POSSIVEL ALTERAR)\n')
    sleep(time)
    print('Escolha Sua Vocação:')
    vocacao = Menu(['Druid', 'Sorcerer', 'Necromancer', 'Paladin', 'Archer', 'Knight', 'Berseker'], obrigatorio=False)
    if vocacao == 'Druid':
        player.voc = Druid(player)
    elif vocacao == 'Sorcerer':
        player.voc = Sorcerer(player)
    elif vocacao == 'Necromancer':
        player.voc = Necromancer(player)
    elif vocacao == 'Paladin':
        player.voc = Paladin(player)
    elif vocacao == 'Archer':
        player.voc = Archer(player)
    elif vocacao == 'Knight':
        player.voc = Knight(player)
    elif vocacao == 'Berseker':
        player.voc = Berseker(player)
    sleep(time)
    print(f'{player.nome_player} Escolheu {vocacao} como vocação!')
    sleep(time)
# print('Bruno: Saiba que neste mundo é matar ou morrer, existem muitos monstros e mestres fortissimos\n')
# sleep(time)
# print('Bruno: Aqui existem os labirintos. Nesses labirintos é onde estão os mais fortes dos monstros e mestres\n')
# sleep(time)
print('Bruno: Quer treinar com um monstro fraco?')
op = Menu(['Sim', 'Não'], obrigatorio=False)
if op == 'Sim':
    troll = Troll()
    mochila = Mochila()
    if not mochila.VerificarItem('Faquinha') and not mochila.VerificarItem('Arco Simples') and not mochila.VerificarItem('Bone Ascent') and not mochila.VerificarItem('Spear'):  
        sleep(time)
        print('Bruno: Me parece que não te nenhuma arma, escolha uma dessas duas:') 
        arm = Menu(['Faquinha      Dano médio: 20', 'Arco Simples (Vem com 25 flechas simples)      Dano médio: 27'], obrigatorio=False)
        if arm[:7] == 'Faquinha':
            arma = Faquinha()
        elif arm[:12] == 'Arco Simples':
            flecha = FlechaSimples()
            mochila.Adicionar_mochila(flecha.name, 25)
            arma = ArcoSimples(flecha)
            print(f'Foi adicionado ')
        mochila.Adicionar_mochila(arma.name, 1)
        player.EquiparArma(arma)
    else:
        print('Qual arma usar?')
        sleep(time)
        armaEscolhida = Menu(mochila.MostrarArmas(False), obrigatorio=False)
        player.EquiparArma(armaEscolhida)
    res = player.ModoAtaque(troll)