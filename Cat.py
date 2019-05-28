'''
*******************Developed by********************************
    
Alfredo Albélis Batista Filho - https://github.com/AlfredoFilho
Brenda Alexsandra Januario - https://github.com/brendajanuario
Cleofas Peres Santos -  https://github.com/CleoPeres
Leonardo Ferrari - https://github.com/LeonardoFerrari
Pedro Bernini - https://github.com/PedroBernini
Vinicius Abrantes - https://github.com/viniciusAbrantes

**************************************************************** 
'''

# import sys
from dataclasses import dataclass
import FuncMenor

tabuleiro = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10),
             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
             (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
             (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10),
             (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
             (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10),
             (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10),
             (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10),
             (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10),
             (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]


@dataclass
class celula:
    def __init__(self, coordenada, total, distanciaComeco, distanciaAteFinal, caminho):
        self.coordenada = coordenada
        self.total = total
        self.distanciaComeco = distanciaComeco
        self.distanciaAteFinal = distanciaAteFinal
        self.caminho = caminho


pai = (5, 5)
bloqueados = [(9, 9), (9, 8), (9, 7), (9, 10)]
saida = (10, 10)


def andarEmVolta(pai, listaAberta, listaFechada):
    expansao = []
    listinha = []
    # lista com as celulas inicias em volta do pai
    expansao = [(pai[0], pai[1] + 1),
                (pai[0] + 1, pai[1] + 1),
                (pai[0] + 1, pai[1]),
                (pai[0], pai[1] - 1),
                (pai[0] - 1, pai[1]),
                (pai[0] - 1, pai[1] + 1)]

    # print("espansao: ", expansao)

    for coord in expansao:
        valido = True
        if coord not in bloqueados and coord in tabuleiro:
            for struc in listaFechada:
                if coord == struc.coordenada:
                    # print("Não colocou (ta na fechada):", coord)
                    valido = False
            if valido == True:
                for struct in listaAberta:
                    if coord == struct.coordenada:
                        # print("Não colocou (ta na aberta):", coord)
                        valido = False
            if valido == True:
                # print("Colocou:", coord)
                listinha.append(coord)

    # print("listinha:", listinha)
    # print("\n")
    return listinha


def preencherstruct(listinha, pai, listaAberta):
    # preencher struct com posicao, distancia e o pai (que ainda é a posição do pai)

    for coordenada in listinha:
        distanciaComeco = FuncMenor.distance(pai, coordenada)
        distanciaAteFinal = FuncMenor.distance(coordenada, saida)
        total = distanciaComeco + distanciaAteFinal

        listaAberta.append(celula(coordenada, total, distanciaComeco, distanciaAteFinal, pai))
    return listaAberta


def ordenarCelulasPorDistancia(listaAberta):
    elementos = len(listaAberta) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if listaAberta[i].total > listaAberta[i + 1].total:
                listaAberta[i], listaAberta[i + 1] = listaAberta[i + 1], listaAberta[i]
                ordenado = False
    return listaAberta

#    for i in range(0, len(listaAberta) - 1):
#        for j in range(i, len(listaAberta) - 1):
#            if listaAberta[j].total > listaAberta[j + 1].total:
#                temp = listaAberta[j]
#                listaAberta[j] = listaAberta[j + 1]
#                listaAberta[j + 1] = temp
#    return listaAberta


def astar(pai, saida):
    listaFechada = []
    listaAberta = []

    a = 0

    distanciaComeco = FuncMenor.distance(pai, saida)
    distanciaAteFinal = FuncMenor.distance(pai, saida)
    total = distanciaComeco + distanciaAteFinal
    listaAberta.append(celula(pai, total, distanciaComeco, distanciaAteFinal, None))
    
    # for struct in listaAberta:
    #     print("Abertos: ", struct.coordenada)
    #     print("Coordenada:                 ", struct.coordenada)
    #     print("Total                 (f):   ", struct.total)
    #     print("Distancia do comeco   (g):   ", struct.distanciaComeco)
    #     print("Distancia ate o final (h):   ", struct.distanciaAteFinal)
    #     print("Caminho:                    ", struct.caminho)
    #     print("\n")

    while pai != saida:

        a = a + 1

        listinha = andarEmVolta(pai, listaAberta, listaFechada)
        listaAberta = preencherstruct(listinha, pai, listaAberta)
        listaAberta = ordenarCelulasPorDistancia(listaAberta)

        cont = 0

        for struct in listaAberta:
            if struct.coordenada == pai:
                listaFechada.append(struct)
                listaAberta.pop(cont)
                break
            cont = cont + 1

        pai = listaAberta[0].coordenada

        # for struct in listaAberta:
        #     print("Abertos: ", struct.coordenada)
        #     print("Coordenada:                 ", struct.coordenada)
        #     print("Total                 (f):   ", struct.total)
        #     print("Distancia do comeco   (g):   ", struct.distanciaComeco)
        #     print("Distancia ate o final (h):   ", struct.distanciaAteFinal)
        #     print("Caminho:                    ", struct.caminho)
        #     print("\n")
        #
        print("Pai: ", pai)
        #
        # for struct in listaFechada:
        #     print("Fechados: ", struct.coordenada)
        #
        # print("\n")

    print("\n")
    for struct in listaAberta:
        if pai == struct.coordenada:
            print("Caminho: ", struct.caminho)
            print("\n")

    print("Quantidade:", a)


astar(pai, saida)
