from Cats.Cat_aStar import aStar
from Cats.Cat_BestFirst import bestFirst
from Cats.Cat_DepthFirst import depthFirst
from Cats.Cat_BreadthFirstSearch import breadthFirstSearch

estadoInicial = (5, 5)

estadoFinal = (0, 10)

bloqueados = [(3, 4), (3, 6), (3 ,8), (2, 7), (2, 8), (4, 5),
              (4, 6), (4, 8), (1, 3), (4, 10), (5, 7), (5, 9),
              (6, 7), (6, 8), (6, 9), (2, 4), (8, 5), (1, 2),
              (2, 2), (3, 2), (4, 3), (5, 4), (6, 4), (7, 4)]

aStar(estadoInicial, estadoFinal, bloqueados)
bestFirst(estadoInicial, estadoFinal, bloqueados)
depthFirst(estadoInicial, estadoFinal, bloqueados)
breadthFirstSearch(estadoInicial, [estadoFinal], bloqueados)