'''
*******************Developed by********************************
    
Alfredo Albelis Batista Filho - https://github.com/AlfredoFilho
Brenda Alexsandra Januario - https://github.com/brendajanuario
Cleofas Peres Santos - https://github.com/CleoPeres

**************************************************************** 
'''

from dataclasses import dataclass
import Cats.Calcular as Calcular
import GifMaker.GifMaker as GifMaker
import os

cat    =  (5, 5)

exits = [(10, 10)]

blocks = (9, 7), (9, 8), (9, 9), (9, 10)

#blocks  = [(3, 4), (3, 6), (3 ,8), (2, 7), (2, 8), (4, 5),
#           (4, 6), (4, 8), (1, 3), (4, 10), (5, 7), (5, 9),
#           (6, 7), (6, 8), (6, 9), (2, 4), (8, 5), (1, 2),
#           (2, 2), (3, 2), (4, 3), (5, 4), (6, 4), (7, 4)]

delayGif = None
dir = 'Gifs/Gif_BreadthFirstSearch.gif'

images = []

positionCat = cat
chosen_exit = exits
positionCatInTuple = tuple(cat)
positionsVisited = []
expandedStates = []

dark_green = "#4a8e52"
light_green = "#61b76b"

def next_move(direction, cat) :
    candidatos = {
        "NW": [(cat[0]-1, cat[1]-1), (cat[0]-1, cat[1])],
        "NE": [(cat[0] - 1, cat[1]), (cat[0]-1, cat[1] + 1)],
        "W" : [(cat[0], cat[1] - 1), (cat[0], cat[1] - 1)],
        "E" : [(cat[0], cat[1] + 1), (cat[0], cat[1] + 1)],
        "SW": [(cat[0] + 1, cat[1] - 1),(cat[0] + 1, cat[1])],
        "SE": [(cat[0] + 1, cat[1]),(cat[0] + 1, cat[1]+1)]
    }
    return candidatos[direction][cat[0]%2]

def breadthFirstSearch (cat, chosen_exit, blocks):
    
    images.append(GifMaker.compute_initial_image(cat, blocks, chosen_exit[0], images))
    
    solutionFound = False
    positionsVisited.append(cat) #add cat position in list of positions visited
    
    while len(positionsVisited) != 0:
        atual = positionsVisited.pop(0) #remove first of list
        
        if atual != cat:
            images.append(GifMaker.fill_dot(atual, "black", images))
            
            print("\n-----------------")
            print("Escolhido:", atual)
        
        if(atual not in blocks and atual in chosen_exit):
            solutionFound = True
            break
        successorStates = findSuccessorPositions(atual, expandedStates, positionsVisited) #call function to walk with the cat and find the next positions
        
        print("Expandidos:")
        
        for el in successorStates:
            print("    Coordenda:",el)
            images.append(GifMaker.fill_dot(el, "gray", images))
        expandedStates.append(atual)

#        os.system("pause")

        for i in range (0, len(successorStates)): #check the new positions to see if they have already been included
            successor = successorStates[i]
            if successor not in expandedStates and successor not in positionsVisited:        
                positionsVisited.append(successorStates[i])
                
    if solutionFound == True:
        movimento = Solution(atual)    
        expandedStates.clear()
        positionsVisited.clear()
        successorStates.clear()
#        print(movimento[-1])
        images[0].save(dir,
           save_all=True,
           append_images=images[1:],
           duration=200,
           loop=0)
        os.remove("GifMaker/ImagemTemp.png")
        os.remove("GifMaker/ImagemTemp2.png")
    return 0
    
predecessorCoordinates={}
predecessorPosition={}

def findSuccessorPositions(cat, expandedStates, positionsVisited):
    coordinates = ["NE","E","SW","SE","W","NW"]
    successorPositions=[]
    for el in coordinates:
        successor = next_move(el, cat)
        if (successor[0]<0 or successor[1]<0 or successor[0]>10 or successor[1]>10):
            continue
        elif(successor in blocks):
            continue
        elif(successor not in expandedStates and successor not in positionsVisited and successor not in blocks):
            successorPositions.append(successor)
            predecessorCoordinates[successor]=el
            predecessorPosition[successor]=cat
            
    return successorPositions
    
def Solution(cat):
    listPositions=[]
    listCoordinates=[]
    aux=cat
    listPositions.append(cat)
    while (aux != tuple(positionCat)):
        listPositions.append(predecessorPosition[aux])
        listCoordinates.append(predecessorCoordinates[aux])
        aux = predecessorPosition[aux]
    for el in listPositions:
        images.append(GifMaker.fill_dot(el, dark_green, images))
    listPositions.reverse()
    for el in listPositions:
        images.append(GifMaker.fill_dot(el, light_green, images))
    print("\nCaminho", listPositions)
    return listCoordinates

print("\n-----------------")
print("Escolhido:",cat)
breadthFirstSearch(positionCatInTuple, chosen_exit, blocks, delayGif)
