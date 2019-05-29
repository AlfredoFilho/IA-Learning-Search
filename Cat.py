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
import FuncMenor
from PIL import Image, ImageDraw

def compute_image_exp(expandidos, cat, blocks, exits) :
    im = Image.open("gameboard.png").convert("RGBA")
    draw = ImageDraw.Draw(im)                
    
    for el in expandidos :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "orange"
        )
    
    for el in exits :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "blue"
        )

    for el in blocks :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.line([init_x+10, init_y+10, end_x-10, end_y-10],
                  fill = "red", width=6)
        draw.line([init_x+10,end_y-10, end_x-10, init_y+10],
                  fill = "red", width=6)

    for el in [cat] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "black"
        )
        
        
        
    del draw
    return im

def compute_image(cat, blocks, exits) :
    im = Image.open("gameboard.png").convert("RGBA")
    draw = ImageDraw.Draw(im)                
        
    for el in exits :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "blue"
        )

    for el in blocks :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.line([init_x+10, init_y+10, end_x-10, end_y-10],
                  fill = "red", width=6)
        draw.line([init_x+10,end_y-10, end_x-10, init_y+10],
                  fill = "red", width=6)

    for el in [cat] :
        shift = el[0] % 2 * 25
        init_x = shift + el[1]*50 + el[1]*5
        end_x  = shift + (el[1]+1)*50 + el[1]*5
        init_y = el[0]*49
        end_y  = (el[0]+1)*49
        draw.ellipse([init_x, init_y, end_x, end_y],
                     fill = "black"
        )
        
        
        
    del draw
    return im

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
    def __init__(self, coordenada, total, distanciaComeco, distanciaAteFinal, pai):
        self.coordenada = coordenada
        self.total = total
        self.distanciaComeco = distanciaComeco
        self.distanciaAteFinal = distanciaAteFinal
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


def andarEmVolta(atual, listaAberta, listaFechada):
    expansao = []
    listinha = []
    # lista com as celulas inicias em volta do pai
    if atual[0] % 2 != 0:

        expansao = [(atual[0], atual[1] + 1),
                        (atual[0] + 1, atual[1] + 1),
                        (atual[0] + 1, atual[1]),
                        (atual[0], atual[1] - 1),
                        (atual[0] - 1, atual[1]),
                        (atual[0] - 1, atual[1] + 1)]
    else:
        expansao = [(atual[0], atual[1] + 1),
                    (atual[0] + 1, atual[1]),
                    (atual[0] + 1, atual[1] - 1),
                    (atual[0], atual[1] - 1),
                    (atual[0] - 1, atual[1] - 1),
                    (atual[0] - 1, atual[1])]

#    print("espansao: ", expansao)

    for coord in expansao:
        valido = True
        if coord not in bloqueados and coord in tabuleiro:
            for struc in listaFechada:
                if coord == struc.coordenada:
#                    print("Não colocou (ta na fechada):", coord)
                    valido = False
            if valido == True:
                for classe in listaAberta:
                    if coord == classe.coordenada:
#                        print("Não colocou (ta na aberta):", coord)
                        valido = False
            if valido == True:
#                print("Colocou:", coord)
                listinha.append(coord)

#    print("listinha:", listinha)
#    print("\n")
    return listinha


def preencherclasse(listinha, cat, atual, listaAberta, listaFechada):
    # preencher classe com posicao, distancia e o pai (que ainda é a posição do pai)

    for coordenada in listinha:
        distanciaComeco = FuncMenor.funcaoG(cat, atual, listaFechada, listaAberta) + 1
        distanciaAteFinal = FuncMenor.funcaoH(coordenada, saida)
        total = distanciaComeco + distanciaAteFinal

        listaAberta.append(celula(coordenada, total, distanciaComeco, distanciaAteFinal, atual))
    
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

def astar(atual, cat, saida):
    images = []
    listaFechada = []
    listaAberta = []

    a = 0

    distanciaComeco = 0
    distanciaAteFinal = FuncMenor.funcaoH(atual, saida)
    total = distanciaComeco + distanciaAteFinal
    listaAberta.append(celula(atual, total, distanciaComeco, distanciaAteFinal, None))
    
#    for classe in listaAberta:
#        print("Coordenada:                 ", classe.coordenada)
#        print("Total                 (f):   ", classe.total)
#        print("Distancia do comeco   (g):   ", classe.distanciaComeco)
#        print("Distancia ate o final (h):   ", classe.distanciaAteFinal)
#        print("Pai:                         ", classe.pai)
#        print("\n")

    while atual != saida:

        a = a + 1

        listinha = andarEmVolta(atual, listaAberta, listaFechada)
        listaAberta = preencherclasse(listinha, cat, atual, listaAberta, listaFechada)
        listaAberta = ordenarCelulasPorDistancia(listaAberta)

        cont = 0

        for classe in listaAberta:
            if classe.coordenada == atual:
                listaFechada.append(classe)
                listaAberta.pop(cont)
                break
            cont = cont + 1

        atual = listaAberta[0].coordenada
#
#        for classe in listaAberta:
#            print("Coordenada:                 ", classe.coordenada)
#            print("Total                 (f):   ", classe.total)
#            print("Distancia do comeco   (g):   ", classe.distanciaComeco)
#            print("Distancia ate o final (h):   ", classe.distanciaAteFinal)
#            print("Pai:                         ", classe.pai)
#            print("\n")
#
#        print("Atual: ", atual)
#
#        for classe in listaFechada:
#            print("Fechados: ", classe.coordenada)
#
#        print("\n")

    aux = True

    b = []

    b.append(atual)

#    print("\n")
    for classe in listaAberta:
        if atual == classe.coordenada:
            atual = classe.pai
            b.append(atual)

    while aux:
        for classe in listaFechada:
            if classe.coordenada == atual:
                atual = classe.pai
                b.append(atual)
                if atual == cat:
                    aux = False

    b.reverse()

#    for el in listaFechada:
#        print(el.coordenada)
    print("Inicio", cat)
    print("\n")
    print("Bloqueios", bloqueados)
    print("\n")
    print("Quantidade:", a)
    print(b)
    lista = []
    
    for c in listaFechada:
        lista.append(c.coordenada)
        images.append(compute_image_exp(lista, cat, bloqueados, exits))
    
    #for el in lista:
     #   images.append(compute_image(el, bloqueados, exits))
    
    images[0].save('game.gif',
                       save_all=True,
                       append_images=images[1:],
                       duration=400,
                       loop=0)
    
astar(atual, cat, saida)