from lib.Armas import *
from lib.Inimigos import *
from lib.Mochila import *
from lib.Player import *

p1 = Player('Bruno')
faca = Faquinha()
curse = Cursed_Skeleton()
troll = Troll()
# print(curse.atacarPlayer(p1))
# print(curse.atacarPlayer(p1))
# print(curse.atacarPlayer(p1))
mochila = Mochila()
mochila.Adicionar_mochila('Escama', 2)
mochila.Adicionar_mochila('Curativo', 10)
mochila.AbrirMochila()
print(p1.atacarMonstro(faca, troll))
print(p1.atacarMonstro(faca, troll))
print(p1.atacarMonstro(faca, troll))
