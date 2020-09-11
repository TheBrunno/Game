from random import randint

class Magia_Cura_All:
    def __init__(self, ply, mag):
        if isinstance(mag, str):
            if mag == 'Kurapa Kwechiedza':
                mag = Cura_Druid_Leve()
        if mag.tipe == 'cura':
            if ply.tipe_voc == mag.voc:
                if ply.mana - mag.precoMana <= 0:
                    print(f'{ply.nome_player} Esta sem mana para essa magia')
                    return
                ply.mana = ply.mana - mag.precoMana
                ply.vida += mag.cura
                if ply.lvl == 1:
                    if ply.vida > ply.vida_initial:
                        ply.vida = ply.vida_initial
                elif ply.vida > ply.lvl * ply.aumentoVida:
                    ply.vida = ply.lvl * ply.aumentoVida
                print(f'{ply.nome_player} Usou a magia \"{mag.name}\" e curou {mag.cura}HP, Ficando com {ply.vida}, gastando {mag.precoMana} de mana')


class Magia_Ataque_All:
    def __init__(self, ply, mst, mga):
        if isinstance(mga, str):
            if mga == 'Kusasimba Kwechando Kurwisa':
                mga = Ataque_Druid_Leve()
        if ply.tipe_voc == mga.voc:
            if mst.vivo:
                if mga.tipe == 'ataque':
                    if ply.mana - mga.precoMana <= 0:
                        print(f'{ply.nome_player} Está sem mana para essa magia')
                        return
                    ply.mana -= mga.precoMana
                    mst.life -= mga.ataque
                    if mst.life <= 0:
                        mst.life = 0
                        mst.vivo = False
                        ply.exp_player += mst.exp
                        mst.Dropar(ply)
                        if ply.exp_player >= ply.upp:
                            ply.Upar()
                            print(f'{ply.nome_player} matou {mst.name} com a magia \"{mga.name}\", gastando {mga.precoMana} de mana1.\nParabens {ply.nome_player}, você upou para o lvl {ply.lvl}..')
                            return
                        print(f'{ply.nome_player} matou {mst.name} com a magia \"{mga.name}\", gastando {mga.precoMana}.\nParabens {ply.nome_player}, você venceu! Ganhou {mst.exp} de exp')
                        return
                    print(f'{ply.nome_player} Ataca {mst.name} com \"{mga.name}\" que ficou com {mst.life}HP')
                    return
            else:
                print(f'{mst.name} Já está morto')
                return


class Cura_Druid_Leve:
    voc = 'druid'
    tipe = 'cura'
    precoMana = 30
    cura = randint(40, 60)
    name = 'Kurapa Kwechiedza'


class Ataque_Druid_Leve:
    voc = 'druid'
    tipe = 'ataque'
    precoMana = 45
    ataque = randint(40, 60)
    name = 'Kusasimba Kwechando Kurwisa'

            
