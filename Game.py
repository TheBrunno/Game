from Module import *
from Inimigos import *


p1 = Player('Bruno')
faca = Faquinha()
orc = Orc()
mino = Minotauro()
troll = Troll()
mochila = Mochila()
mochila.Adicionar_mochila('Escama', 2)
mochila.Adicionar_mochila('Escama', 4)
print(p1.ataque(faca, troll))
print(p1.ataque(faca, troll))
print(p1.ataque(faca, troll))
