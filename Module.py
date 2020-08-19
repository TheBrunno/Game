from random import randint
from Inimigos import *
from Armas import *
import json


class Player:
    vivo = True
    lvl = 1
    vida = lvl * 100
    def __init__(self, nome):
        self.nome_player = nome
        self.exp_player = 0

    def atacarMonstro(self, arm, monster):
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
            return f'{self.nome_player} ataca {monster.name} que ficou com {monster.life} de vida'


class Mochila:
    def __init__(self):
        self.mochila = 'mochila.json'


    def Adicionar_mochila(self, item, qtd):
        arquivo_json = open('mochila.json', 'r')
        dic = json.load(arquivo_json)
        arquivo_json.close()
        passou = False
        cont = 0
        for k in dic:
            cont += 1
            if str(k) == str(item):
                dic[item] += qtd
                json_file = open('mochila.json', 'w')
                json.dump(dic, json_file, indent=4)
                json_file.close()
                passou = True
                break
            elif cont == int(len(dic)):
                if passou:
                    return
                else:
                    dic[item] = qtd
                    json_file = open('mochila.json', 'w')
                    json.dump(dic, json_file, indent=4)
                    json_file.close()
                    break

    def MostrarMochila(self):
        with open('mochila.json', 'r') as archive_json:
            dic = json.load(archive_json)
            for k, v in dic.items():
                print(f'{k.ljust(20)} {v}')