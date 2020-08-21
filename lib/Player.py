from lib.Item import LifePotion, ManaPotion
from lib.Mochila import Mochila

class Player:
    vivo = True
    lvl = 1
    vida = lvl * 100
    mana = lvl * 150
    def __init__(self, nome):
        self.nome_player = nome
        self.exp_player = 0

    def Usar(self, item):
        mochila = Mochila()
        if mochila.VerificarItem(item.name):
            if item.name == 'Life Potion':
                self.vida += item.Add
                print(f'\'{self.nome_player}\' Usou {item.name} e recuperou {item.Add} de vida\nFicando com {self.vida}HP')
                if self.vida > self.lvl * 100:
                    self.vida = self.lvl * 100
            elif item.name == 'Mana potion':
                self.mana += item.Add
                print(f'\'{self.nome_player}\' Usou {item.name} e recuperou {item.Add} de mana\nFicando com {self.mana}MN')
                if self.mana > self.lvl * 150:
                    self.mana = self.lvl * 150
            mochila.RetirarItem(item.name)

    def atacarMonstro(self, arm, monster):
        if self.vivo:
            monster.life -= arm.ataque
            if monster.life <= 0:
                monster.life = 0
                if monster.vivo:
                    monster.vivo = False
                    self.exp_player += monster.exp
                    monster.Dropar(self)
                    return f'{self.nome_player} matou {monster.name}.\n{self.nome_player} ganhou {monster.exp} de exp'
                else:
                    return f'{monster.name} ja esta morto'
            else:
                return f'{self.nome_player} ataca \'{monster.name}\' com {arm.name}, que ficou com {monster.life} de vida'
        else:
            return f'{self.nome_player} não pode atacar pois esta morto'

