# -*- coding: utf-8 -*-
'''
*******************Developed by********************************
    
Alfredo Albélis Batista Filho - https://github.com/AlfredoFilho
Brenda Alexsandra Januário - https://github.com/brendajanuario
Cléofas Peres Santos -  https://github.com/CleoPeres
Leonardo Ferrari - https://github.com/LeonardoFerrari
Pedro Bernini - https://github.com/PedroBernini
Vinicius Abrantes - https://github.com/viniciusAbrantes

*************************************************************** 
'''

from dataclasses import dataclass
import Calcular
import GifMaker
import os

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
             (10,0), (10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), (10,8), (10,9), (10,10)]

light_green = "#61b76b"

@dataclass
class no:
    def __init__(self, coordenada, pai):
        self.coordenada = coordenada
        self.pai = pai

estadoInicial = (5, 5)

estadoFinal = (10, 10)

bloqueados = [(9, 7), (9, 8), (9, 9), (9, 10)]

images = []

def expandir(estadoInicial, estadoEscolhido, bloqueados, estadoFinal, visitados):

    if estadoEscolhido[0] % 2 != 0: #Se a linha do gato for par
        listaExpansaoSuja = [(estadoEscolhido[0], estadoEscolhido[1] + 1),      #Leste
                             (estadoEscolhido[0] + 1, estadoEscolhido[1] + 1),  #Sudeste
                             (estadoEscolhido[0] + 1, estadoEscolhido[1]),      #Sudoeste
                             (estadoEscolhido[0], estadoEscolhido[1] - 1),      #Oeste
                             (estadoEscolhido[0] - 1, estadoEscolhido[1]),      #Noroeste
                             (estadoEscolhido[0] - 1, estadoEscolhido[1] + 1)]  #Nordeste
    else:
        listaExpansaoSuja = [(estadoEscolhido[0], estadoEscolhido[1] + 1),      #Leste
                             (estadoEscolhido[0] + 1, estadoEscolhido[1]),      #Sudeste
                             (estadoEscolhido[0] + 1, estadoEscolhido[1] - 1),  #Sudoeste
                             (estadoEscolhido[0], estadoEscolhido[1] - 1),      #Oeste
                             (estadoEscolhido[0] - 1, estadoEscolhido[1] - 1),  #Noroeste
                             (estadoEscolhido[0] - 1, estadoEscolhido[1])]      #Nordeste
    
    #Retirar da lista suja bloqueados e fora do tabuleiro
    listaExpansao = []
    for coordenada in listaExpansaoSuja:
        if coordenada not in bloqueados and coordenada in tabuleiro and coordenada not in visitados:
            if(coordenada != estadoFinal):
                aux = GifMaker.fill_dot(coordenada, "gray", images)
                if aux != images[-1]:
                    images.append(aux)
            listaExpansao.append(coordenada)
    
    return listaExpansao

def preencherNo(listaExpansao, estadoInicial, estadoEscolhido, visitados):

    print("\n---------")
    print("Estado escolhido:",estadoEscolhido)
    print("Expandidos:")
    
    adjacentes = []
    for coordenada in listaExpansao :
        adjacentes.append(no(coordenada, estadoEscolhido))
       
        print("    Coordenada:", coordenada)
    print("\nLista visitados:", visitados)
#    os.system("pause") 
    return adjacentes

def backtrack(visitados):
    count = len(visitados) - 1
    
    while(count != 0):
        count -= 1
        listaExpansao = expandir(estadoInicial, visitados[count], bloqueados, estadoFinal, visitados)
        if len(listaExpansao) != 0:
            return listaExpansao
        
    print("Sem saída")
    images[0].save('depthFirst.gif',
               save_all=True,
               append_images=images[1:],
               duration=40,
               loop=0)
    os.remove("ImagemTemp.png")
    return None

def depthFirst(estadoInicial, estadoFinal):
    
    estadoEscolhido = estadoInicial
    
    images.append(GifMaker.compute_initial_image(estadoInicial, bloqueados, estadoFinal, images))
    
    visitados = [estadoInicial]
    
    while estadoEscolhido != estadoFinal :  
        
        listaExpansao = expandir(estadoInicial, estadoEscolhido, bloqueados, estadoFinal, visitados)
        
        if len(listaExpansao) == 0:
            listaExpansao = backtrack(visitados)
            if listaExpansao == None:
                return 0
            
        adjacentes = preencherNo(listaExpansao, estadoInicial, estadoEscolhido, visitados)
        estadoEscolhido = adjacentes[0].coordenada

        visitados.append(estadoEscolhido)
        
        if estadoEscolhido != estadoInicial :
            images.append(GifMaker.fill_dot(estadoEscolhido, light_green, images))
        
#        print("Atual: ", estadoEscolhido)
    
    images[0].save('depthFirst.gif',
                       save_all=True,
                       append_images=images[1:],
                       duration=200,
                       loop=0)
        
    os.remove("ImagemTemp.png")
        
depthFirst(estadoInicial, estadoFinal)