'''
*******************Developed by********************************
    
Alfredo Albélis Batista Filho - https://github.com/AlfredoFilho
Brenda Alexsandra Januário - https://github.com/brendajanuario
Cléofas Peres Santos -  https://github.com/CleoPeres
Leonardo Ferrari - https://github.com/LeonardoFerrari
Pedro Bernini - https://github.com/PedroBernini
Vinicius Abrantes - https://github.com/viniciusAbrantes

**************************************************************** 
'''

# import sys
from dataclasses import dataclass
import Calcular
import GifMaker

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
    def __init__(self, coordenada, total_F, distanciaComeco_G, distanciaAteFinal_H, pai):
        self.coordenada = coordenada
        self.total_F = total_F
        self.distanciaComeco_G = distanciaComeco_G
        self.distanciaAteFinal_H = distanciaAteFinal_H
        self.pai = pai

#import sys
#cat         = tuple(eval(sys.argv[1]))
#bloqueados  = eval(sys.argv[2])
#exits       = eval(sys.argv[3])
#atual = cat
#
#saida = exits[0]

cat = (5, 5)
atual = cat
bloqueados = [(9, 9)]
saida = (10, 10)

exits = [saida]


def expandirEmVolta(atual, listaAberta, listaFechada):
    listaExpansaoSuja = []
    listaExpansao = []
    
    # lista com as celulas inicias em volta do pai
    if atual[0] % 2 != 0:

        listaExpansaoSuja = [(atual[0], atual[1] + 1),
                             (atual[0] + 1, atual[1] + 1),
                             (atual[0] + 1, atual[1]),
                             (atual[0], atual[1] - 1),
                             (atual[0] - 1, atual[1]),
                             (atual[0] - 1, atual[1] + 1)]
    else:
        listaExpansaoSuja = [(atual[0], atual[1] + 1),
                             (atual[0] + 1, atual[1]),
                             (atual[0] + 1, atual[1] - 1),
                             (atual[0], atual[1] - 1),
                             (atual[0] - 1, atual[1] - 1),
                             (atual[0] - 1, atual[1])]

    for coord in listaExpansaoSuja:
        valido = True
        if coord not in bloqueados and coord in tabuleiro:
            for struc in listaFechada:
                if coord == struc.coordenada:
                    valido = False
            if valido == True:
                for classe in listaAberta:
                    if coord == classe.coordenada:
                        valido = False
            if valido == True:
                listaExpansao.append(coord)

    return listaExpansao


def preencherclasse(listaExpansao, cat, atual, listaAberta, listaFechada):
    # preencher classe com posicao, distancia e o pai (que ainda é a posição do pai)

    for coordenada in listaExpansao:
        distanciaComeco_G = Calcular.G(cat, atual, listaFechada, listaAberta) + 1
        distanciaAteFinal_H = Calcular.H(coordenada, saida)
        total_F = distanciaComeco_G + distanciaAteFinal_H

        listaAberta.append(celula(coordenada, total_F, distanciaComeco_G, distanciaAteFinal_H, atual))
    
    return listaAberta


def ordenarCelulasPorDistancia(listaAberta):

    elementos = len(listaAberta) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if listaAberta[i].total_F > listaAberta[i + 1].total_F:
                listaAberta[i], listaAberta[i + 1] = listaAberta[i + 1], listaAberta[i]
                ordenado = False
    return listaAberta

def astar(atual, cat, saida):
    images = []
    listaFechada = []
    listaAberta = []

    a = 0

    distanciaComeco_G = 0
    distanciaAteFinal_H = Calcular.H(atual, saida)
    total_F = distanciaComeco_G + distanciaAteFinal_H
    listaAberta.append(celula(atual, total_F, distanciaComeco_G, distanciaAteFinal_H, None))

    while atual != saida:

        a = a + 1

        listaExpansao = expandirEmVolta(atual, listaAberta, listaFechada)
        listaAberta = preencherclasse(listaExpansao, cat, atual, listaAberta, listaFechada)
        listaAberta = ordenarCelulasPorDistancia(listaAberta)

        cont = 0

        for classe in listaAberta:
            if classe.coordenada == atual:
                listaFechada.append(classe)
                listaAberta.pop(cont)
                break
            cont = cont + 1

        atual = listaAberta[0].coordenada

    aux = True

    listaComMelhorCaminho = []

    listaComMelhorCaminho.append(atual)

    for classe in listaAberta:
        if atual == classe.coordenada:
            atual = classe.pai
            listaComMelhorCaminho.append(atual)

    while aux:
        for classe in listaFechada:
            if classe.coordenada == atual:
                atual = classe.pai
                listaComMelhorCaminho.append(atual)
                if atual == cat:
                    aux = False

    listaComMelhorCaminho.reverse()

    print("Inicio", cat)
    print("\n")
    print("Bloqueios", bloqueados)
    print("\n")
    print("Quantidade de escolhas:", a)
    print(listaComMelhorCaminho)
    lista = []
    
    for c in listaFechada:
        lista.append(c.coordenada)
        images.append(GifMaker.compute_image_exp(lista, cat, bloqueados, exits))
    
    for el in listaComMelhorCaminho:
        images.append(GifMaker.compute_image(el, bloqueados, exits))
    
    images[0].save('game.gif',
                       save_all=True,
                       append_images=images[1:],
                       duration=400,
                       loop=0)
    
astar(atual, cat, saida)