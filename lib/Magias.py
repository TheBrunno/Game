class Magia_Cura_All():
    def __init__(self, ply, mag):
        if ply.tipe_voc == mag.voc:
            if ply.mana - mag.precoMana <= 0:
                print(f'{ply.nome_player} Esta sem mana para essa magia')
                return
            ply.mana = ply.mana - mag.precoMana
            ply.vida += mag.cura
            if ply.vida > ply.vida_initial:
                ply.vida = ply.vida_initial
            print(f'{ply.nome_player} Usou a magia \"{mag.name}\" e curou {mag.cura}HP, Ficando com {ply.vida}, gastando {mag.precoMana} de mana')

class Cura_Druid_Leve():
    voc = 'druid'
    precoMana = 30
    cura = 50
    name = 'Kurapa Kwechiedza'

            
