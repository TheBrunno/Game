from random import randint
from lib.Mochila import Mochila


class ArmasBrancas:
    pass

class Arcos:
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

    
class Faquinha(ArmasBrancas):
    name = 'Faquinha'
    ataque = randint(10, 20)
    Gastaveis = False
    atacavel = True
    equipado = False

class Espada(ArmasBrancas):
    name = 'Espada'
    ataque = randint(15, 25)
    Gastaveis = False
    atacavel = True
    equipado = False


class Mace(ArmasBrancas):
    name = 'Mace'
    ataque = randint(25, 38)
    Gastaveis = False
    atacavel = True
    equipado = False


class FlechaSimples(Flechas):
    name = 'Flecha Simples'
    ataque = randint(22, 32)
    Gastaveis = True
    atacavel = False
    equipado = False

class ArcoSimples(Arcos):
    name = 'Arco Simples'
    ataque = 0
    Gastaveis = False
    atacavel = False
    equipado = False
