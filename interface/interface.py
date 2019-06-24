# -*- coding: utf-8 -*-
from tkinter import *

gato = None
saida = None
bloqueados = []
SELECTED = "BLOQUEIOS"

# CONFIGURAÇÕES DA JANELA
root = Tk()
root.geometry("1280x720+0+0")
root.title("Buscas Heurísticas")
root.configure(background='#707070')
               
               
# FUNCOES GERAIS
def bloquearLiberar(botao) :
    if botao not in bloqueados :
        bloqueados.append(botao)
        lblBloqueios["text"] = lblBloqueios["text"] + "," + botao
    else :
        bloqueados.remove(botao)
        lblBloqueios["text"] = ""
        for el in bloqueados :
            lblBloqueios["text"] = lblBloqueios["text"] + "," + el

def btnSelectGato_click() :
    SELECTED = "GATO"
    print(SELECTED)
            
# FUNCOES BOTÕES TABULEIRO
def btn00_click() :
    bloquearLiberar("(0, 0)")

def btn01_click() :
    bloquearLiberar("(0, 1)")
               
               
# BLOQUEIOS
FirstFrame = Frame(root, width=1280, height=30)
FirstFrame.pack(side=TOP)
lblBloqueios = Label(FirstFrame, font=('calibri', 15), text="Lista de Bloqueados", width=128)
lblBloqueios.grid(row=0, column=0)

# GATO
SecondFrame = Frame(root, width=1280, height=30)
SecondFrame.pack(side=TOP)          
lblGato = Label(SecondFrame, font=('calibri', 15), text="Posição do Gato", width=128)
lblGato.grid(row=0, column=0)

# SAIDA
ThirdFrame = Frame(root, width=1280, height=30)
ThirdFrame.pack(side=TOP)
lblSaida = Label(ThirdFrame, font=('calibri', 15), text="Posição da Saída", width=128)
lblSaida.grid(row=0, column=0)


#BOTÕES GERAIS
btnSelectGato = Button(root, width=20,text="Selecionar Gato", command=btnSelectGato_click)
btnSelectGato.place(x=900,y=100)

#BOTÕES LINHA 0
btn00 = Button(root, width=3,text="(0,0)", command=btn00_click)
btn00.place(x=100,y=100)

btn01 = Button(root, width=3,text="(0,1)", command=btn01_click)
btn01.place(x=160,y=100)


root.mainloop()