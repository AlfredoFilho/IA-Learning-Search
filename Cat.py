'''
*******************Developed by********************************
    
Alfredo Albelis Batista Filho - https://github.com/AlfredoFilho
Brenda Alexsandra Januario - https://github.com/brendajanuario
Cleofas Peres Santos -  https://github.com/CleoPeres
Pedro Bernini - https://github.com/PedroBernini
Vinicius Abrantes - https://github.com/viniciusAbrantes

**************************************************************** 
'''

#import sys
from dataclasses import dataclass
import FuncMenor

tabuleiro = [(0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7),(0, 8),(0, 9),(0, 10),
             (1, 0),(1, 1),(1, 2),(1, 3),(1, 4),(1, 5),(1, 6),(1, 7),(1, 8),(1, 9),(1, 10),
             (2, 0),(2, 1),(2, 2),(2, 3),(2, 4),(2, 5),(2, 6),(2, 7),(2, 8),(2, 9),(2, 10),
             (3, 0),(3, 1),(3, 2),(3, 3),(3, 4),(3, 5),(3, 6),(3, 7),(3, 8),(3, 9),(3, 10),
             (4, 0),(4, 1),(4, 2),(4, 3),(4, 4),(4, 5),(4, 6),(4, 7),(4, 8),(4, 9),(4, 10),
             (5, 0),(5, 1),(5, 2),(5, 3),(5, 4),(5, 5),(5, 6),(5, 7),(5, 8),(5, 9),(5, 10),
             (6, 0),(6, 1),(6, 2),(6, 3),(6, 4),(6, 5),(6, 6),(6, 7),(6, 8),(6, 9),(6, 10),
             (7, 0),(7, 1),(7, 2),(7, 3),(7, 4),(7, 5),(7, 6),(7, 7),(7, 8),(7, 9),(7, 10),
             (8, 0),(8, 1),(8, 2),(8, 3),(8, 4),(8, 5),(8, 6),(8, 7),(8, 8),(8, 9),(8, 10),
             (9, 0),(9, 1),(9, 2),(9, 3),(9, 4),(9, 5),(9, 6),(9, 7),(9, 8),(9, 9),(9, 10),
             (10, 0),(10, 1),(10, 2),(10, 3),(10, 4),(10, 5),(10, 6),(10, 7),(10, 8),(10, 9),(10, 10)]
    
@dataclass
class celula:
    def __init__(self, coordenada, distancia, caminho = []):
        self.coordenada = coordenada
        self.distancia = distancia
        self.caminho = caminho

cat = (5, 5)
gato = cat
bloqueados = []
saida = (10, 10)
lista_aberta = []
lista_fechada = []
listaStructAbertas = []

def andarEmVolta():
    em_volta = []
    #lista com as celulas inicias em volta do gato
    em_volta = [((gato[0], gato[1] + 1)),
               ((gato[0] + 1, gato[1] + 1)),
               ((gato[0] + 1, gato[1])),
               ((gato[0], gato[1] - 1)),
               ((gato[0] - 1, gato[1])),
               ((gato[0] - 1, gato[1] + 1))]
    return em_volta

#Verificar se as celulas iniciais em volta não são bloqueados e não estão fora do limite do tabuleiro para poder iniciar a lista aberta
def verificaCelulasEmVolta(em_volta):
    
    for el in em_volta:
        if el not in bloqueados and el in tabuleiro:
            lista_aberta.append(el)

def preencherStruct():
    #preencher struct com posicao, distancia e o pai (que ainda é a posição do gato)
    for el in lista_aberta:
        dist = FuncMenor.distance(el, saida)
        listaStructAbertas.append(celula(el, dist, gato))
    
    
def ordenarCelulasPorDistancia():
    for i in range (0, len(listaStructAbertas)-1):
        for j in range (i, len(listaStructAbertas)-1):
            if listaStructAbertas[j].distancia > listaStructAbertas[j+1].distancia:
                temp =  listaStructAbertas[j]
                listaStructAbertas[j] = listaStructAbertas[j+1]
                listaStructAbertas[j+1] = temp

def Astar():
    em_volta = andarEmVolta()
    verificaCelulasEmVolta(em_volta)
    preencherStruct()
    ordenarCelulasPorDistancia()
    
    if(listaStructAbertas[0].coordenada == saida)
        andar = listaStructAbertas[0].coordenada    
        return andar
    
    else:
        while (gato != saida):
            gato = listaStructAbertas[0].coordenada
            em_volta = andarEmVolta()
            verificaCelulasEmVolta(em_volta)
            preencherStruct()
            ordenarCelulasPorDistancia()
            

    return andar

andar = Astar()

print(andar)
      
for el in listaStructAbertas:
    print("----------------")
    
    print("Caminho:     ", el.caminho)
    print("Coordenada:  ", el.coordenada)
    print("Distancia:   ", el.distancia)
    print("Saida:       ", saida)
    print("----------------")
    print("\n")
    
