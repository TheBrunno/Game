from lib.Item import LifePotion, ManaPotion, Meat
from lib.Mochila import Mochila
from lib.Inimigos import Monsters
from lib.Armas import Espada, Faquinha, ArcoSimples, FlechaSimples, Mace, Spear, BoneAscent
from lib.Armaduras import HelmetLeather, ArmorLeather, LegsLeather, BootsLeather
from time import sleep


def LeiaInt(msg, maxn, minn=1, obrigatorio=True):
    while True:
        try:
            num = int(input(msg))
        except:
            print('Digite um numero inteiro')
        else:
            if obrigatorio:
                if num == 999:
                    return 999
            if num > maxn or num < minn:
                print(f'Digite um numero entre {minn} e {maxn}')
                continue
            return num


def Menu(lst, num=False, obrigatorio=True):
    print('-=' * 10)
    for ind, ele in enumerate(lst):
        print(f'{ind + 1} - {ele}')
    print('-=' * 10)
    if obrigatorio:
        print('999 para VOLTAR')
    op = LeiaInt('Digite sua opção: ', maxn=len(lst), minn=1 ,obrigatorio=obrigatorio)
    if not num:
        if obrigatorio:
            if op == 999:
                return 999
        return lst[op - 1]
    elif num:
        return op

time = 0
class Player:
    voc = None
    vivo = True
    lvl = 1
    vida = mana = aumentoMana = aumentoVida = defesa = 0
    equip = equipHead = equipArmor = equipLegs = equipBoots = None
    def __init__(self, nome):
        self.nome_player = nome
        self.exp_player = 0
        self.upp = 100
    

    def Usar(self, item):
        mochila = Mochila()
        if mochila.VerificarItem(item.name):
            sleep(time)
            if item.tipe == 'Life':
                self.vida += item.Add
                if self.vida > self.lvl * 100:
                    self.vida = self.lvl * 100
                print(f'\'{self.nome_player}\' Usou {item.name} e recuperou {item.Add} de vida\nFicando com {self.vida} de HP')
            elif item.tipe == 'Mana':
                self.mana += item.Add
                if self.mana > self.lvl * 150:
                    self.mana = self.lvl * 150
                print(f'\'{self.nome_player}\' Usou {item.name} e recuperou {item.Add} de mana\nFicando com {self.mana} de MANA')
            mochila.RetirarItem(item.name)
        else:
            sleep(time)
            print(f'{self.nome_player} Não tem {item.name} na mochila...')


    def atacarMonstro(self, monster):
        mochila = Mochila()
        if self.equip == None:
            return f'É necessario equipar uma arma antes de usar'
        if mochila.VerificarItem(self.equip.name):
            if self.vivo:
                if monster.vivo:
                    if self.equip.Gastaveis:
                        if self.equip.tipe == 'lança':
                            if not mochila.VerificarItem(self.equip.name):
                                return f'{self.nome_player} não tem esse item'
                            else:
                                mochila.RetirarItem(self.equip.name)
                        else:
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
                            self.vida = self.lvl * self.aumentoVida
                            self.mana = self.lvl * self.aumentoMana
                            return f'{self.nome_player} matou {monster.name}.\nParabens {self.nome_player}, você upou para o lvl {self.lvl}..'
                        return f'{self.nome_player} matou {monster.name}.\nParabens {self.nome_player}, você venceu! Ganhou {monster.exp} de exp'
                    return f'{self.nome_player} ataca \'{monster.name}\' com {self.equip.name}, que ficou com {monster.life} de vida'
            else:
                return f'{self.nome_player} não pode atacar pois esta morto'
        else:
            return f'{self.nome_player} não tem esse item'


    def ModoAtaque(self, monster):
        atacado = False
        listaAtk = ['Atacar monstro', 'Equipar item', 'Abrir Mochila', 'Usar itens', 'Conversar', 'Fugir']
        while monster.vivo:
            if self.vivo:
                sleep(time)
                print(f'\nFalta {self.upp - self.exp_player}XP Para você upar para o lvl {self.lvl + 1}')
                print(f'LIFE:{self.vida}   MANA:{self.mana}   LVL:{self.lvl}')
                op = Menu(listaAtk, obrigatorio=False)
                if op == 'Atacar monstro':
                    sleep(time)
                    print(self.atacarMonstro(monster))
                    atacado = True
                    sleep(time)
                    if monster.vivo:
                        print(monster.atacarPlayer(self))
                elif op == 'Abrir Mochila':
                    mochila = Mochila()
                    mochila.AbrirMochila()
                elif op == 'Usar itens':
                    mochila = Mochila()
                    sleep(time)
                    resp = 0
                    while isinstance(resp, int):
                        args = mochila.Mostrar_Itens_Curar(False)
                        resp = Menu(args)
                        if resp == 999:
                            break
                        elif resp == 'Mana Potion':
                            cura = ManaPotion()
                        elif resp == 'Life Potion':
                            cura = LifePotion()
                        elif resp == 'Meat':
                            cura = Meat()
                        self.Usar(cura)
                elif op == 'Conversar':
                    if monster.conversavel:
                        from random import randint
                        porc = randint(0, 3)
                        if porc == 3 and not atacado:
                            sleep(time)
                            print(monster.msgTru)
                            sleep(time)
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
                            sleep(time)
                            print(monster.atacarPlayer(self))
                            sleep(time)
                    else:
                        sleep(time)
                        print(monster.msgNot)
                        sleep(time)
                        print(monster.atacarPlayer(self))
                elif op == 'Fugir':
                    from random import randint
                    porc = randint(0, 2)
                    if porc == 1 or porc == 2:
                        sleep(time)
                        print(f'{self.nome_player} fugiu da luta com {monster.name}...')
                        return 'Fugiu'
                    else:
                        sleep(time)
                        print(f'{self.nome_player} não conseguiu fugir da luta com {monster.name}')
                        sleep(time)
                        print(monster.atacarPlayer(self))
                        sleep(time)
                elif op == 'Equipar item':
                    equip = Menu(['Equipar Armas', 'Equipar Armaduras'])
                    mochila = Mochila()
                    sleep(time)
                    if equip == 'Equipar Armas':
                        lst = Menu(mochila.MostrarArmas(False))
                        sleep(time)
                        self.EquiparArma(lst)
                    elif equip == 'Equipar Armaduras':
                        while True:
                            lst = Menu(mochila.MostrarArmas(False, True))
                            sleep(time)
                            if lst == 999:
                                break
                            self.EquiparArmadura(lst)
            else:
                return

    def EquiparArma(self, equip):
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
            elif equip == 'Spear':
                arma = Spear()
            elif equip == 'Bone Ascent':
                arma = BoneAscent()
            self.equip = arma
        else:
            if isinstance(equip, int):
                if equip == 999:
                    return
            if equip.tipe == 'arma branca' or equip.tipe == 'arco' or equip.tipe == 'arco':
                self.equip = equip
        sleep(time)
        print(f'{self.nome_player} Equipou {self.equip.name}')
        sleep(time)
    

    def EquiparArmadura(self, armadura):
        sleep(time)
        if isinstance(armadura, str):
            if armadura == 'Capacete De Couro':
                self.equipHead = HelmetLeather(self)
            elif armadura == 'Armadura De Couro':
                self.equipArmor = ArmorLeather(self)
            elif armadura == 'Calça De Couro':
                self.equipLegs = LegsLeather(self)
            elif armadura == 'Bota De Couro':
                self.equipBoots = BootsLeather(self)
            print(f'{self.nome_player} Equipou {armadura}')
        else:
            if isinstance(armadura, int):
                if armadura == 999:
                    return
            if armadura.tipe == 'helmet':
                self.equipHead = armadura
            elif armadura.tipe == 'armor':
                self.equipArmor = armadura
            elif armadura.tipe == 'legs':
                self.equipLegs = armadura
            elif armadura.tipe == 'boots':
                self.equipBoots = armadura
            print(f'{self.nome_player} Equipou {armadura.name}')
        sleep(time)