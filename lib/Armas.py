from random import randint
from lib.Mochila import Mochila


class ArmasBrancas:
    tipe = 'arma branca'

class Arcos:
    tipe = 'arco'
    def __init__(self, Flecha):
        mochila = Mochila()
        if mochila.VerificarItem(Flecha.name):
            self.qtd = mochila.VerificarItem(Flecha.name, True)
            self.ataque = Flecha.ataque
            self.Gastaveis = True
            self.atacavel = True
            self.flecha_name = Flecha.name


class Flechas:
    pass


class Lanca:
    tipe = 'lança'

    
class Faquinha(ArmasBrancas):
    name = 'Faquinha'
    ataque = randint(5, 15)
    Gastaveis = False
    atacavel = True
    equipado = False

class Espada(ArmasBrancas):
    name = 'Espada'
    ataque = randint(10, 20)
    Gastaveis = False
    atacavel = True
    equipado = False


class Mace(ArmasBrancas):
    name = 'Mace'
    ataque = randint(20, 30)
    Gastaveis = False
    atacavel = True
    equipado = False


class FlechaSimples(Flechas):
    name = 'Flecha Simples'
    ataque = randint(8, 20)
    Gastaveis = True
    atacavel = False
    equipado = False

class ArcoSimples(Arcos):
    name = 'Arco Simples'
    ataque = 0
    Gastaveis = False
    atacavel = False
    equipado = False


class Spear(Lanca):
    name = 'Spear'
    ataque = randint(15, 35)
    Gastaveis = True
    atacavel = True
    equipado = False


class BoneAscent(ArmasBrancas):
    name = 'Bone Ascent'
    ataque = randint(35, 51)
    Gastaveis = False
    atacavel = True
    equipado = False
