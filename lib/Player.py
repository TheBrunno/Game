from lib.Item import LifePotion, ManaPotion, Meat
from lib.Mochila import Mochila
from lib.Inimigos import Monsters
from lib.Armas import Espada, Faquinha, ArcoSimples, FlechaSimples, Mace, Spear, BoneAscent
from lib.Armaduras import HelmetLeather, ArmorLeather, LegsLeather, BootsLeather
from lib.Magias import Cura_Druid_Leve, Magia_Cura_All, Magia_Ataque_All, Ataque_Druid_Leve
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


def Menu(lst, obrigatorio=True, qtd=False):
    print('-=' * 10)
    if not qtd:
        for ind, ele in enumerate(lst):
            print(f'{ind + 1} - {ele}')
    if qtd:
        cont = 0
        for ind, ele in enumerate(lst[0]):
            print(f'{ind + 1} - {lst[1][cont]} {ele} ')
            cont += 1
    print('-=' * 10)
    if obrigatorio:
        print('999 para VOLTAR')
    if qtd:
        op = LeiaInt('Digite sua opção: ', maxn=len(lst[0]), minn=1 ,obrigatorio=obrigatorio)
    else:
        op = LeiaInt('Digite sua opção: ', maxn=len(lst), minn=1 ,obrigatorio=obrigatorio)
    if obrigatorio:
        if op == 999:
            return 999
        if qtd:
            return lst[0][op - 1]
    return lst[op - 1]

time = 0
class Player:
    vivo = True
    vida = mana = aumentoMana = aumentoVida = defesa = vidaMax = ManaMax = vida_initial = mana_initial = dano_bonus = 0
    equip = equipHead = equipArmor = equipLegs = equipBoots = voc = tipe_voc = voc_tipe = None
    magias_Liberadas_Ataque = []
    magias_Liberadas_Cura = []
    def __init__(self, nome):
        self.nome_player = nome
        self.exp_player = 0
        self.upp = 100
        self.lvl = 1

    @property
    def lvl(self):
        return self.__lvl

    @lvl.setter
    def lvl(self, value):
        self.__lvl = value
        if self.__lvl == 1 and self.tipe_voc == None:
            return
        if self.tipe_voc == 'druid':
            if self.__lvl == 1:
                magia = 'Kurapa Kwechiedza', 'Cura'
            if self.__lvl == 2:
                magia = 'Kusasimba Kwechando Kurwisa', 'Ataque'
        elif self.tipe_voc == 'sorcerer':
            if self.__lvl == 1:
                magia = 'Chiedza Chemoto Mushonga', 'Cura'
            if self.__lvl == 2:
                magia = 'Kushaya Simba Kwemoto', 'Ataque'
        elif self.tipe_voc == 'necromancer':
            if self.__lvl == 1:
                magia = 'Tuka Mushonga', 'Cura'
            if self.__lvl == 2:
                magia = 'Kushaya Simba Kwekufa', 'Ataque'
        elif self.tipe_voc == 'paladin':
            if self.__lvl == 1:
                magia = 'Chitsvene Kupodzwa Kwechiedza', 'Cura'
            if self.__lvl == 2:
                magia = 'Kurwiswa Kutsvene Chiedza', 'Ataque'
        elif self.tipe_voc == 'archer':
            if self.__lvl == 1:
                magia = 'Kupora Kwepanyama', 'Cura'
            if self.__lvl == 2:
                magia = 'Kurwisa Kwepanyama', 'Ataque'
        elif self.tipe_voc == 'knight':
            if self.__lvl == 1:
                magia = 'Kupora Kwakareruka', 'Cura'
            if self.__lvl == 2:
                magia = 'Kurwiswa Kwakakomba Chiedza', 'Ataque'
        elif self.tipe_voc == 'berseker':
            if self.__lvl == 1:
                magia = 'Kutsamwa Kupora Chiedza', 'Cura'
            if self.__lvl == 2:
                magia = 'Kudenha Zvine Hasha', 'Ataque'
        if magia[1] == 'Ataque':
            self.magias_Liberadas_Ataque.append(magia[0])
        elif magia[1] == 'Cura':
            self.magias_Liberadas_Cura.append(magia[0])

    def Upar(self):
        self.upp += 300
        self.exp_player = 0
        self.lvl += 1
        self.vida = self.lvl * self.aumentoVida
        self.mana = self.lvl * self.aumentoMana

    def Usar(self, item):
        mochila = Mochila()
        if mochila.VerificarItem(item.name):
            sleep(time)
            if item.tipe == 'Life':
                self.vida += item.Add
                if self.lvl == 1:
                    if self.vida > self.vida_initial:
                        self.vida = self.vida_initial
                        print(f'\'{self.nome_player}\' Usou {item.name} e encheu sua vida, ficando com {self.vida} de HP')
                elif self.vida > self.lvl * self.aumentoVida:
                    self.vida = self.lvl * self.aumentoVida
                    print(f'\'{self.nome_player}\' Usou {item.name} e encheu sua vida, ficando com {self.vida} de HP')
                else:
                    print(f'\'{self.nome_player}\' Usou {item.name} e recuperou {item.Add} de vida\nFicando com {self.vida} de HP')
            elif item.tipe == 'Mana':
                self.mana += item.Add
                if self.lvl == 1:
                    if self.mana > self.mana_initial:
                        self.mana = self.mana_initial
                        print(f'\'{self.nome_player}\' Usou {item.name} e encheu sua mana, ficando com {self.vida} de MANA')
                elif self.mana > self.lvl * self.aumentoMana:
                    self.mana = self.lvl * self.aumentoMana
                    print(f'\'{self.nome_player}\' Usou {item.name} e encheu sua mana, ficando com {self.vida} de MANA')
                else:
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
                    if self.tipe_voc == 'berseker' or self.tipe_voc == 'knight':
                        if self.equip.tipe == 'arma branca':
                            self.equip.ataque += self.dano_bonus + (self.dano_bonus * self.dano_bonus / 100)
                    elif self.tipe_voc == 'paladin' or self.tipe_voc == 'archer':
                        if self.equip.tipe == 'arco' or self.equip.tipe == 'spear':
                            self.equip.ataque += self.dano_bonus + (self.dano_bonus * self.dano_bonus / 100)
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
                    monster.life = int(monster.life)
                    if monster.life <= 0:
                        monster.life = 0
                        monster.vivo = False
                        self.exp_player += monster.exp
                        monster.Dropar(self)
                        if self.exp_player >= self.upp:
                            self.Upar()
                            return f'{self.nome_player} matou {monster.name}.\nParabens {self.nome_player}, você upou para o lvl {self.lvl}..'
                        return f'{self.nome_player} matou {monster.name}.\nParabens {self.nome_player}, você venceu! Ganhou {monster.exp} de exp'
                    return f'{self.nome_player} ataca \'{monster.name}\' com {self.equip.name}, que ficou com {monster.life} de vida'
            else:
                return f'{self.nome_player} não pode atacar pois esta morto'
        else:
            return f'{self.nome_player} não tem esse item'


    def ModoAtaque(self, monster):
        atacado = False
        listaAtk = ['Atacar monstro', 'Equipar item', 'Abrir Mochila', 'Curar', 'Conversar', 'Fugir']
        while monster.vivo:
            if self.vivo:
                sleep(time)
                print(f'\nFalta {self.upp - self.exp_player}XP Para você upar para o lvl {self.lvl + 1}')
                print(f'LIFE:{self.vida}   MANA:{self.mana}   LVL:{self.lvl}')
                op = Menu(listaAtk, obrigatorio=False)
                if op == 'Atacar monstro':
                    resp = Menu(['Atacar com Magia', 'Atacar com Arma'])
                    sleep(time)
                    if resp == 999:
                        continue
                    if resp == 'Atacar com Arma':
                        print(self.atacarMonstro(monster))
                        atacado = True
                    elif resp == 'Atacar com Magia':
                        resp = Menu(self.magias_Liberadas_Ataque)
                        if resp == 999:
                            continue
                        Magia_Ataque_All(self, monster, resp)
                        atacado = True
                    if monster.vivo:
                        print(monster.atacarPlayer(self))
                    sleep(time)
                elif op == 'Abrir Mochila':
                    mochila = Mochila()
                    mochila.AbrirMochila()
                elif op == 'Curar':
                    resp = Menu(['Curar com Magia', 'Curar com Itens'])
                    if resp == 'Curar com Magia':
                        resp = Menu(self.magias_Liberadas_Cura)
                        if resp == 999:
                            continue
                        Magia_Cura_All(self,resp)
                    elif resp == 'Curar com Itens':
                        while True:
                            mochila = Mochila()
                            sleep(time)
                            args = mochila.Mostrar_Itens_Curar(False, True)
                            resp = Menu(args, qtd=True)
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
                                self.Upar()
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