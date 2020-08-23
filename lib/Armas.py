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
    ataque = randint(20, 30)
    Gastaveis = False
    atacavel = True

class Espada(ArmasBrancas):
    name = 'Espada'
    ataque = randint(35, 45)
    Gastaveis = False
    atacavel = True

class FlechaSimples(Flechas):
    name = 'Flecha Simples'
    ataque = randint(25, 35)
    Gastaveis = True
    atacavel = False

class ArcoSimples(Arcos):
    name = 'Arco Simples'
    ataque = 0
    Gastaveis = False
    atacavel = False
