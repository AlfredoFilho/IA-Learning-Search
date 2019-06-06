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

from dataclasses import dataclass
import Calcular
import GifMaker
import os

#import sys
#cat         = tuple(eval(sys.argv[1]))
#bloqueados  = eval(sys.argv[2])
#saida       = eval(sys.argv[3])

#cat = input("Posição inicial: ")
#cat = tuple(int(x.strip()) for x in cat.split(','))

cat = (5, 5)
saida = (10, 10)

bloqueados = [(9, 7), (9, 8), (9, 9), (9, 10)]


#saida = input("Saida: ")
#saida = tuple(int(x.strip()) for x in saida.split(','))

catTemporario = cat #----------> Gato que irá "andar" até encontrar a saida

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

#Struct
@dataclass
class celula:
    def __init__(self, coordenada, total_F, distanciaComeco_G, distanciaAteFinal_H, pai):
        self.coordenada = coordenada
        self.total_F = total_F
        self.distanciaComeco_G = distanciaComeco_G
        self.distanciaAteFinal_H = distanciaAteFinal_H
        self.pai = pai

dark_green = "#4a8e52"
light_green = "#61b76b"

def expandirEmVolta(cat, catTemporario, listaAberta, listaFechada, images, bloqueados, saida):
    # lista com as celulas inicias em volta do pai
    listaExpansaoSuja = []
    
    #Lista expansao limpa (sem bloqueados e dentro do tabuleiro)
    listaExpansao = []
    
    if catTemporario[0] % 2 != 0: #Se a linha do gato for par
        listaExpansaoSuja = [(catTemporario[0], catTemporario[1] + 1),      #
                             (catTemporario[0] + 1, catTemporario[1] + 1),  #
                             (catTemporario[0] + 1, catTemporario[1]),      #
                             (catTemporario[0], catTemporario[1] - 1),      #
                             (catTemporario[0] - 1, catTemporario[1]),      #
                             (catTemporario[0] - 1, catTemporario[1] + 1)]  #
    else:
        listaExpansaoSuja = [(catTemporario[0], catTemporario[1] + 1),      #
                             (catTemporario[0] + 1, catTemporario[1]),      #
                             (catTemporario[0] + 1, catTemporario[1] - 1),  #
                             (catTemporario[0], catTemporario[1] - 1),      #
                             (catTemporario[0] - 1, catTemporario[1] - 1),  #
                             (catTemporario[0] - 1, catTemporario[1])]      #
    
    
    #Retirar da lista suja bloqueados e fora do tabuleiro
    for coord in listaExpansaoSuja:
        valido = True
        if coord not in bloqueados and coord in tabuleiro:
            for struc in listaFechada:
                if coord == struc.coordenada:
                    valido = False
            if valido == True:
                for struct in listaAberta:
                    if coord == struct.coordenada:
                        valido = False
            if valido == True:
                if(coord != saida):
                    images.append(GifMaker.fill_dot(coord, "gray", images))
                listaExpansao.append(coord)
    
    return listaExpansao


def preencherStruct(listaExpansao, cat, catTemporario, listaAberta, listaFechada):

    for coordenada in listaExpansao:
        distanciaComeco_G = Calcular.G(cat, catTemporario, listaFechada, listaAberta) + 1
        distanciaAteFinal_H = Calcular.H(coordenada, saida)
        total_F = distanciaComeco_G + distanciaAteFinal_H

        listaAberta.append(celula(coordenada, total_F, distanciaComeco_G, distanciaAteFinal_H, catTemporario))
        
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

def aStar(catTemporario, cat, saida):
    images = []
    
    #Fazer imagem inicial do gif - cat, bloqueios e saida
    images.append(GifMaker.compute_initial_image(cat, bloqueados, saida, images))
    
    listaFechada = [] #lista visitados
    listaAberta = []  #lista não visitados
    
    contadorEscolhasPai = 0

    #estrutura para a coordenada inicial
    distanciaComeco_G = 0
    distanciaAteFinal_H = Calcular.H(catTemporario, saida)
    total_F = distanciaComeco_G + distanciaAteFinal_H
    listaAberta.append(celula(catTemporario, total_F, distanciaComeco_G, distanciaAteFinal_H, None))

#-----------------------------------------------------------------------
    while catTemporario != saida:

        contadorEscolhasPai = contadorEscolhasPai + 1

        listaExpansao = expandirEmVolta(cat, catTemporario, listaAberta, listaFechada, images, bloqueados, saida)
        listaAberta = preencherStruct(listaExpansao, cat, catTemporario, listaAberta, listaFechada)
        listaAberta = ordenarCelulasPorDistancia(listaAberta)
        
        #encontrar na lista aberta coordenada expandida e colocar na lista fechada
        cont = 0
        for struct in listaAberta:
            if struct.coordenada == catTemporario:
                listaFechada.append(struct)
                listaAberta.pop(cont)
                break
            cont = cont + 1

        catTemporario = listaAberta[0].coordenada
        
        if(catTemporario != saida):
            images.append(GifMaker.fill_dot(catTemporario, "black" , images))
        else:
            images.append(GifMaker.fill_dot(catTemporario, light_green, images))
 #-----------------------------------------------------------------------
    listaComMelhorCaminho = []
    listaComMelhorCaminho.append(catTemporario)
    
    #Encontra coordenada que gerou a expansao para a saida
    for struct in listaAberta:
        if catTemporario == struct.coordenada:
            catTemporario = struct.pai
            listaComMelhorCaminho.append(catTemporario)
    
    #Fazer caminho inverso pela lista fechada até a coordenada inicial(cat)
    aux = True
    while aux:
        for struct in listaFechada:
            if struct.coordenada == catTemporario:
                catTemporario = struct.pai
                listaComMelhorCaminho.append(catTemporario)
                if catTemporario == cat:
                    aux = False
    
    #Fazer parte do gif que volta da saida até o inicio
    for coordenada in listaComMelhorCaminho:
        if coordenada == cat or coordenada == saida:
            continue
        else:
            images.append(GifMaker.fill_dot(coordenada, light_green, images))
    
    #inverter a lista
    listaComMelhorCaminho.reverse()

    #Fazer parte do gif que anda até o fim
    for coordenada in listaComMelhorCaminho:
        if coordenada == cat:
            continue
        else:
            images.append(GifMaker.fill_dot(coordenada, dark_green, images))
    
    #salvar gif
    images[0].save('game.gif',
                       save_all=True,
                       append_images=images[1:],
                       duration=200,
                       loop=0)
    print("Gif Gerado")
    print("\n")
    print("Inicio", cat)
    print("\n")
    print("Bloqueios", bloqueados)
    print("\n")
    print("Quantidade de escolhas:", contadorEscolhasPai)
    print("\n")
    print("Lista melhor caminho: ", listaComMelhorCaminho)
    
    os.remove("ImagemTemp.png") 
aStar(catTemporario, cat, saida)