from lib.Item import LifePotion, ManaPotion
from lib.Mochila import Mochila
from lib.Inimigos import Monsters
from lib.Armas import Espada, Faquinha, ArcoSimples, FlechaSimples, Mace
from time import sleep


def LeiaInt(msg, maxn, minn=1):
    while True:
        try:
            num = int(input(msg))
        except:
            print('Digite um numero inteiro')
        else:
            if num > maxn or num < minn:
                print(f'Digite um numero entre {minn} e {maxn}')
                continue
            return num


def Menu(lst, num=False):
    print('-=' * 10)
    for ind, ele in enumerate(lst):
        print(f'{ind + 1} - {ele}')
    print('-=' * 10)
    op = LeiaInt('Digite sua opção: ', len(lst))
    if not num:
        return lst[op - 1]
    elif num:
        return op


class Player:
    vivo = True
    lvl = 1
    vida = lvl * 100
    mana = lvl * 150
    equip = None
    def __init__(self, nome):
        self.nome_player = nome
        self.exp_player = 0
        self.upp = 100
    

    def Usar(self, item):
        mochila = Mochila()
        if mochila.VerificarItem(item.name):
            if item.name == 'Life Potion':
                self.vida += item.Add
                if self.vida > self.lvl * 100:
                    self.vida = self.lvl * 100
                print(f'\'{self.nome_player}\' Usou {item.name} e recuperou {item.Add} de vida\nFicando com {self.vida}HP')
            elif item.name == 'Mana Potion':
                self.mana += item.Add
                if self.mana > self.lvl * 150:
                    self.mana = self.lvl * 150
                print(f'\'{self.nome_player}\' Usou {item.name} e recuperou {item.Add} de mana\nFicando com {self.mana}MANA')
            mochila.RetirarItem(item.name)


    def atacarMonstro(self, monster):
        mochila = Mochila()
        if self.equip == None:
            return f'É necessario equipar uma arma antes de usar'
        if mochila.VerificarItem(self.equip.name):
            if self.vivo:
                if monster.vivo:
                    if self.equip.Gastaveis:
                        qtd = int(mochila.VerificarItem(self.equip.flecha_name, True))
                        if qtd <= 0:
                            self.equip.atacavel = False
                            return f'{self.nome_player} não pode atacar pois acabou as flechas'
                        mochila.RetirarItem(self.equip.flecha_name)
                    monster.life -= self.equip.ataque
                    if monster.life <= 0:
                        monster.life = 0
                        monster.vivo = False
                        self.exp_player += monster.exp
                        monster.Dropar(self)
                        if self.exp_player >= self.upp:
                            self.upp += 300
                            self.exp_player = 0
                            self.lvl += 1
                            self.vida = self.lvl * 100
                            self.mana = self.lvl * 150
                            return f'{self.nome_player} matou {monster.name}.\nParabens {self.nome_player}, você upou para o lvl {self.lvl}..'
                        return f'{self.nome_player} matou {monster.name}.\nParabens {self.nome_player}, você venceu! Ganhou {monster.exp} de exp'
                    return f'{self.nome_player} ataca \'{monster.name}\' com {self.equip.name}, que ficou com {monster.life} de vida'
            else:
                return f'{self.nome_player} não pode atacar pois esta morto'
        else:
            return f'{self.nome_player} não tem esse item'


    def ModoAtaque(self, monster):
        atacado = False
        listaAtk = ['Atacar monstro', 'Equipar item', 'Usar Potions', 'Conversar', 'Fugir']
        while monster.vivo:
            if self.vivo:
                Magia_Arma = ['Atacar Com Magia', 'Atacar com Armas']
                print(f'\nFalta {self.upp - self.exp_player}XP Para você upar para o lvl {self.lvl + 1}')
                print(f'LIFE:{self.vida}   MANA:{self.mana}   LVL:{self.lvl}')
                op = Menu(listaAtk)
                if op == 'Atacar monstro':
                    sleep(1)
                    print(self.atacarMonstro(monster))
                    atacado = True
                    sleep(1)
                    if monster.vivo:
                        print(monster.atacarPlayer(self))
                elif op == 'Usar Potions':
                    mochila = Mochila()
                    sleep(1)
                    while True:
                        mochila.MostrarPots()
                        resp = str(input('999 para\nDigite sua opção: [Mana/Life]: ')).lower()
                        if resp == 'mana' or resp == 'mana potion':
                            manapot = ManaPotion()
                            self.Usar(manapot)
                            break
                        elif resp == 'life' or resp == 'life potion':
                            lifepot = LifePotion()
                            self.Usar(lifepot)
                            break
                        elif resp == '999':
                            break
                        print('=-' * 10)
                        print('ERRO! DIGITE UMA OPÇÃO VALIDA [Mana/Life]')
                elif op == 'Conversar':
                    if monster.conversavel:
                        from random import randint
                        porc = randint(0, 3)
                        if porc == 3 and not atacado:
                            sleep(2)
                            print(monster.msgTru)
                            sleep(1)
                            self.exp_player += monster.exp
                            if self.exp_player >= self.upp:
                                self.upp += 300
                                self.exp_player = 0
                                self.lvl += 1
                                self.vida = self.lvl * 100
                                self.mana = self.lvl * 150
                                print(f'{self.nome_player} conversou com {monster.name}. e entraram num acordo...\nParabens {self.nome_player}, você upou para o lvl {self.lvl}..')
                                return
                            print(f'{self.nome_player} conversou com {monster.name} e entraram num acordo...\nParabens, você ganhou {monster.exp}EXP.')
                            return
                        else:
                            print(monster.msgNot)
                            sleep(2)
                            print(monster.atacarPlayer(self))
                            sleep(1)
                    else:
                        sleep(2)
                        print(monster.msgNot)
                        sleep(1)
                elif op == 'Fugir':
                    from random import randint
                    porc = randint(0, 2)
                    if porc == 1 or porc == 2:
                        sleep(2)
                        print(f'{self.nome_player} fugiu da luta com {monster.name}...')
                        return 'Fugiu'
                    else:
                        sleep(1)
                        print(f'{self.nome_player} não conseguiu fugir da luta com {monster.name}')
                        sleep(2)
                        print(monster.atacarPlayer(self))
                        sleep(1)
                elif op == 'Equipar item':
                    mochila = Mochila()
                    lst = Menu(mochila.MostrarArmas(False))
                    self.Equipar(lst)

    def Equipar(self, equip):
        if isinstance(equip, str):
            if equip == 'Faquinha':
                arma = Faquinha()
            elif equip == 'Espada':
                arma = Espada()
            elif equip == 'Arco Simples':
                flecha = FlechaSimples()
                arma = ArcoSimples(flecha)
            elif equip == 'Mace':
                arma = Mace()
            self.equip = arma
        else:
            self.equip = equip
        sleep(1)
        print(f'{self.nome_player} Equipou {self.equip.name}')
        sleep(2)
