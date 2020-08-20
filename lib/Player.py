class Player:
    vivo = True
    lvl = 1
    vida = lvl * 100
    def __init__(self, nome):
        self.nome_player = nome
        self.exp_player = 0

    def atacarMonstro(self, arm, monster):
        if self.vivo:
            monster.life -= arm.ataque
            if monster.life <= 0:
                monster.life = 0
                if monster.vivo:
                    monster.vivo = False
                    self.exp_player += monster.exp
                    monster.Dropar(self)
                    return f'{self.nome_player} matou {monster.name}.\n{self.nome_player} ganhou {monster.exp} de exp'
                else:
                    return f'{monster.name} ja esta morto'
            else:
                return f'{self.nome_player} ataca \'{monster.name}\' com {arm.name}, que ficou com {monster.life} de vida'
        else:
            return f'{self.nome_player} não pode atacar pois esta morto'
