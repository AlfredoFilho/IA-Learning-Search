from Cats.Cat_aStar import aStar
from Cats.Cat_BestFirst import bestFirst
from Cats.Cat_DepthFirst import depthFirst

estadoInicial = (5, 5)
estadoFinal = (10, 10)
bloqueados = [(9, 7), (9, 8), (9, 9), (9, 10)]

depthFirst(estadoInicial, estadoFinal, bloqueados)
bestFirst(estadoInicial, estadoFinal, bloqueados)
aStar(estadoInicial, estadoFinal, bloqueados)