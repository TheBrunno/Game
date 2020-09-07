import json
from time import sleep

class Mochila:
    def Adicionar_mochila(self, item, qtd=1):
        arquivo_json = open('_mochila.json', 'r')
        dic = json.load(arquivo_json)
        arquivo_json.close()
        passou = False
        cont = 0
        if qtd == 0:
            qtd = 1
        for k in dic:
            cont += 1
            if str(k) == str(item):
                dic[item] += qtd
                json_file = open('_mochila.json', 'w')
                json.dump(dic, json_file, indent=4)
                json_file.close()
                passou = True
                break
        if passou:
            return
        else:
            dic[item] = qtd
            json_file = open('_mochila.json', 'w')
            json.dump(dic, json_file, indent=4)
            json_file.close()

    def AbrirMochila(self):
        with open('_mochila.json', 'r') as archive_json:
            dic = json.load(archive_json)
            sleep(0.5)
            print('=-' * 14)
            for k, v in dic.items():
                sleep(0.5)
                if v == 0:
                    continue
                print(f' {k.ljust(20)}{v}')
            sleep(0.5)
            print('=-' * 14)


    def VerificarItem(self, name, qtd=False):
        with open('_mochila.json', 'r') as archive_json:
            dicionario_json = json.load(archive_json)
            if not qtd:
                cont = 0
                for k in dicionario_json:
                    cont += 1
                    if k == name:
                        return True
                    elif cont == len(dicionario_json):
                        return False
            else:
                cont = 0
                for k, v in dicionario_json.items():
                    cont += 1
                    if k == name:
                        return v
                    elif cont == len(dicionario_json):
                        return False

    def RetirarItem(self, item, qtd=1):
        mochila = Mochila()
        dic2 = {}
        if mochila.VerificarItem(item):
            arquivo_json = open('_mochila.json', 'r')
            dic = json.load(arquivo_json)
            arquivo_json.close()
            for k, v in dic.items():
                if k == item:
                    if int(v) == 1 or int(v) == 0:
                        continue
                    else:
                        v -= qtd
                dic2[k] = v
            with open('_mochila.json', 'w') as json_file:
                json.dump(dic2, json_file, indent=4)

    def Mostrar_Itens_Curar(self, usuario=True):
        with open('_mochila.json', 'r') as json_file:
            dic = json.load(json_file)
            args = []
            print('=-' * 10)
            for k, v in dic.items():
                if k == 'Life Potion' or k == 'Mana Potion' or k == 'Meat':
                    if usuario:
                        print(f'{k}: {v}')
                    else:
                        args.append(k)
            if not usuario:
                return args
            

    def MostrarArmas(self, usuario=True, equipament=False):
        with open('_mochila.json', 'r') as json_file:
            dic = json.load(json_file)
            if usuario:
                for k , v in dic.items():
                    if not equipament:
                        if k == 'Faquinha' or k == 'Espada' or k == 'Arco Simples' or k == 'Flecha Simples' or k == 'Mace' or k == 'Spear' or k == 'Bone Ascent':
                            print('=-' * 10)
                            if usuario:
                                print(f'{k}: {v}')
                    else:
                        if k == 'Capacete De Couro' or k == 'Armadura De Couro' or k == 'Calça De Couro' or k == 'Bota De Couro':
                            print('=-' * 10)
                            if usuario:
                                print(f'{k}: {v}')
            if not usuario:
                arms = []
                equips = []
                for k in dic:
                    if k == 'Flecha Simples':
                        continue
                    else:
                        if not equipament:
                            if k == 'Arco Simples' or k == 'Faquinha' or k == 'Espada' or k == 'Mace' or k == 'Spear' or k == 'Bone Ascent':
                                arms.append(k)
                        else:
                            if k == 'Capacete De Couro' or k == 'Armadura De Couro' or k == 'Calça De Couro' or k == 'Botas De Couro':
                                equips.append(k)
                if not equipament:
                    return arms
                return equips
