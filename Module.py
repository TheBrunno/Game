from random import randint
from Inimigos import *
from Armas import *
import json


class Player:
    lvl = 1
    vida = lvl * 100
    def __init__(self, nome):
        self.nome_player = nome
        self.exp_player = 0

    def ataque(self, arm, monster):
        monster.life -= arm.ataque
        if monster.life <= 0:
            monster.life = 0
            if monster.vivo:
                monster.vivo = False
                self.exp_player += monster.exp
                return f'{self.nome_player} matou {monster.name}.\n{self.nome_player} ganhou {monster.exp} de exp'
            else:
                return f'{monster.name} ja esta morto'
        else:
            return f'{self.nome_player} atacou {monster.name} que ficou com {monster.life} de vida'


class Mochila:
    def __init__(self):
        self.mochila = 'mochila.json'


    def Adicionar_mochila(self, item, qtd):
        arquivo_json = open('mochila.json', 'r')
        dic = json.load(arquivo_json)
        arquivo_json.close()
        for k in dic:
            if str(k) == str(item):
                dic[item] += qtd
                json_file = open('mochila.json', 'w')
                json.dump(dic, json_file, indent=4)
                json_file.close()
                    