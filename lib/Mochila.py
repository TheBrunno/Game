import json


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

    def AbrirMochila(self):
        with open('mochila.json', 'r') as archive_json:
            dic = json.load(archive_json)
            print('=-' * 14)
            for k, v in dic.items():
                print(f' {k.ljust(20)}{v}')
            print('=-' * 14)