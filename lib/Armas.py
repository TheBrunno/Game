from random import randint


class ArmasBrancas:
    pass

class Arco:
    pass

class Faquinha(ArmasBrancas):
    name = 'Faquinha'
    ataque = randint(10, 20)

class Espada(ArmasBrancas):
    name = 'Espada'
    ataque = randint(15, 25)
