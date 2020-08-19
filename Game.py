from Module import *
from Inimigos import *

p1 = Player('Bruno')
faca = Faquinha()
orc = Orc()
mino = Minotauro()
troll = Troll()
print(mino.atacarPlayer(p1))
print(mino.atacarPlayer(p1))
print(mino.atacarPlayer(p1))
mochila = Mochila()
mochila.Adicionar_mochila('Escama', 2)
mochila.Adicionar_mochila('Curativo', 10)
mochila.MostrarMochila()
print(p1.atacarMonstro(faca, troll))
print(p1.atacarMonstro(faca, troll))
print(p1.atacarMonstro(faca, troll))
