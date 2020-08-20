import json

class Mochila:
    def __init__(self):
        self.mochila = '_mochila.json'


    def Adicionar_mochila(self, item, qtd):
        arquivo_json = open('_mochila.json', 'r')
        dic = json.load(arquivo_json)
        arquivo_json.close()
        passou = False
        cont = 0
        for k in dic:
            cont += 1
            if str(k) == str(item):
                dic[item] += qtd
                json_file = open(self.mochila, 'w')
                json.dump(dic, json_file, indent=4)
                json_file.close()
                passou = True
                break
            elif cont == int(len(dic)):
                if passou:
                    return
                else:
                    dic[item] = qtd
                    json_file = open(self.mochila, 'w')
                    json.dump(dic, json_file, indent=4)
                    json_file.close()
                    break

    def AbrirMochila(self):
        with open('mochila.json', 'r') as archive_json:
            dic = json.load(archive_json)
            print('=-' * 14)
            for k, v in dic.items():
                if v == 0:
                    continue
                print(f' {k.ljust(20)}{v}')
            print('=-' * 14)


    def VerificarItem(self, name, qtd=False):
        with open(self.mochila, 'r') as archive_json:
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
                        return f'{k}: {v}'
                    elif cont == len(dicionario_json):
                        return False
                
