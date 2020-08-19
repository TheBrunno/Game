class Monsters:
    def atacarPlayer(self, player):
        player.vida -= self.ataque
        if player.vida <= 0:
            player.vida = 0
            if player.vivo:
                player.vivo = False
                return f'{player.nome_player} foi morto por {self.name}'
            else:
                return f'{player.nome_player} ja esta morto'
        return f'{self.name} ataca {player.nome_player} que ficou com {player.vida} de vida'



class Troll(Monsters):
    name = 'Troll'
    life = 50
    ataque = 10
    exp = 15
    vivo = True


class Orc(Monsters):
    name = 'Orc'
    life = 100
    ataque = 20
    exp = 30
    vivo = True


class Minotauro(Monsters):
    name = 'Minotauro'
    life = 150
    ataque = 30
    exp = 40
    vivo = True