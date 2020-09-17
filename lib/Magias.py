from random import randint

class Magia_Cura_All:
    def __init__(self, ply, mag):
        if isinstance(mag, str):
            if mag == 'Kurapa Kwechiedza':
                mag = Cura_Druid_Leve()
            if mag == 'Chiedza Chemoto Mushonga':
                mag = Cura_Sorcerer_Leve()
            if mag == 'Tuka Mushonga':
                mag = Cura_Necromancer_Leve()
            if mag == 'Chitsvene Kupodzwa Kwechiedza':
                mag = Cura_Paladin_Leve()
            if mag == 'Kurwisa Kwepanyama':
                mag = Cura_Archer_Leve()
            if mag == 'Kupora Kwakareruka':
                mag = Cura_Knight_Leve()
            if mag == 'Kutsamwa Kupora Chiedza':
                mag = Cura_Berseker_Leve()
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
            if mga == 'Kushaya Simba Kwemoto':
                mga = Ataque_Sorcerer_Leve()
            if mga == 'Kushaya Simba Kwekufa':
                mga = Ataque_Necromancer_Leve()
            if mga == 'Kurwiswa Kutsvene Chiedza':
                mga = Ataque_Paladin_Leve()
            if mga == 'Kupora Kwepanyama':
                mga = Ataque_Archer_Leve()
            if mga == 'Kurwiswa Kwakakomba Chiedza':
                mga = Ataque_Knight_Leve()
            if mga == 'Kudenha Zvine Hasha':
                mga = Ataque_Berseker_Leve()
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
                            print(f'{ply.nome_player} matou {mst.name} com a magia \"{mga.name}\", gastando {mga.precoMana} de mana.\nParabens {ply.nome_player}, você upou para o lvl {ply.lvl}..')
                            return
                        print(f'{ply.nome_player} matou {mst.name} com a magia \"{mga.name}\", gastando {mga.precoMana} de mana.\nParabens {ply.nome_player}, você venceu! Ganhou {mst.exp} de exp')
                        return
                    print(f'{ply.nome_player} Ataca {mst.name} com \"{mga.name}\" e gastou {mga.precoMana} de mana\n{mst.name} ficou com {mst.life}HP')
                    return
            else:
                print(f'{mst.name} Já está morto')
                return


class Magia_Druid:
    voc = 'druid'

class Magia_Sorcerer:
    voc = 'sorcerer'
    
class Magia_Necromancer:
    voc = 'necromancer'
    
class Magia_Paladin:
    voc = 'paladin'
    
class Magia_Archer:
    voc = 'archer'
    
class Magia_Knight:
    voc = 'knight'

class Magia_Berseker:
    voc = 'berseker'


# Magias Druid
class Cura_Druid_Leve(Magia_Druid):
    tipe = 'cura'
    precoMana = 30
    cura = randint(10, 20)
    name = 'Kurapa Kwechiedza'

class Ataque_Druid_Leve(Magia_Druid):
    tipe = 'ataque'
    precoMana = 45
    ataque = randint(10, 20)
    name = 'Kusasimba Kwechando Kurwisa'

# Magias Sorcerer
class Cura_Sorcerer_Leve(Magia_Sorcerer):
    tipe = 'cura'
    precoMana = 30
    cura = randint(10, 20)
    name = 'Chiedza Chemoto Mushonga'

class Ataque_Sorcerer_Leve(Magia_Sorcerer):
    tipe = 'ataque'
    precoMana = 50
    ataque = randint(12, 22)
    name = 'Kushaya Simba Kwemoto'

# Magias Necromancer
class Cura_Necromancer_Leve(Magia_Necromancer):
    tipe = 'cura'
    precoMana = 60
    cura = randint(8, 18)
    name = 'Tuka Mushonga'

class Ataque_Necromancer_Leve(Magia_Necromancer):
    tipe = 'ataque'
    precoMana = 70
    ataque = randint(15, 27)
    name = 'Kushaya Simba Kwekufa'

# Magias Paladin
class Cura_Paladin_Leve(Magia_Paladin):
    tipe = 'cura'
    precoMana = 40
    cura = randint(10, 20)
    name = 'Chitsvene Kupodzwa Kwechiedza'

class Ataque_Paladin_Leve(Magia_Paladin):
    tipe = 'ataque'
    precoMana = 30
    ataque = randint(15, 25)
    name = 'Kurwiswa Kutsvene Chiedza'

# Magias Archer
class Cura_Archer_Leve(Magia_Archer):
    tipe = 'cura'
    precoMana = 40
    cura = randint(8, 18)
    name = 'Kupora Kwepanyama'

class Ataque_Archer_Leve(Magia_Archer):
    tipe = 'ataque'
    precoMana = 30
    ataque = randint(18, 28)
    name = 'Kurwisa Kwepanyama'

# Magias Knight
class Cura_Knight_Leve(Magia_Knight):
    tipe = 'cura'
    precoMana = 20
    cura = randint(8, 18)
    name = 'Kupora Kwakareruka'

class Ataque_Knight_Leve(Magia_Knight):
    tipe = 'ataque'
    precoMana = 70
    ataque = randint(15, 25)
    name = 'Kurwiswa Kwakakomba Chiedza'

# Magias Berseker
class Cura_Berseker_Leve(Magia_Berseker):
    tipe = 'cura'
    precoMana = 20
    cura = randint(5, 15)
    name = 'Kutsamwa Kupora Chiedza'

class Ataque_Berseker_Leve(Magia_Berseker):
    tipe = 'ataque'
    precoMana = 30
    ataque = randint(20, 30)
    name = 'Kudenha Zvine Hasha'
