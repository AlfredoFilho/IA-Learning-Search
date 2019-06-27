# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk

gato = []
saida = []
bloqueados = []
SELECTED = "GATO"

# CONFIGURAÇÕES DA JANELA
root = Tk()
root.geometry("1280x720+0+0")
root.title("Buscas Heurísticas")
root.configure(background='#707070')
             
# CLASSE BOTÃO
class CustomButton(tk.Canvas) :
    def __init__(self, parent, width, height, color, command = None, padding = 4):
        tk.Canvas.__init__(self, parent, borderwidth = 1, 
            relief="raised", highlightthickness = 0)
        self.command = command
        
        self.padding = padding
        self.create_oval((padding,padding,
            width+padding, height+padding), outline="black", fill=color)
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0) + padding
        height = (y1-y0) + padding
        self.configure(width=width, height = height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        
    def paint(self, color) :
        width,height = 35,35
        padding = self.padding
        self.configure(relief="raised")
        self.create_oval((padding,padding,
                          width+padding, height+padding), outline="black", fill=color)
    
        
    def _on_press(self, event) :
        global SELETED             
        
        if SELECTED == "GATO" :
            self.paint("orange")
        elif SELECTED == "SAIDA" :
            self.paint("blue")
        elif SELECTED == "BLOQUEIOS" :
            self.paint("red")
        
    def _on_release(self, event) :
        self.configure(relief="raised")
        if self.command is not None :
            self.command()
               
# FUNÇÕES DE SELEÇÃO
def mostrarListas() :
    if gato != [] :
        lblGato["text"] = "Posição do Gato: " + str(gato[0])
    else :
        lblGato["text"] = "Posição do Gato: "

    if saida != [] :
        lblSaida["text"] = "Posição da Saida: " + str(saida[0])
    else :
        lblSaida["text"] = "Posição da Saida: "
        
    lblBloqueios["text"] = "Lista de Bloqueados: "
    for el in bloqueados :
        lblBloqueios["text"] = lblBloqueios["text"] + ", " + str(el)
    
def selectGato(casa, botao) :
    if casa in bloqueados :
        bloqueados.remove(casa)
    if saida != [] and casa == saida[0] :
        saida.clear()
    if gato == [] :
        gato.append(casa)
        gato.append(botao)
    else :
        gato[0] = casa
        gato[1].paint("white")
        gato[1] = botao
        gato[1].paint("orange")
        
    mostrarListas()

def selectSaida(casa, botao) :
    if casa in bloqueados :
        bloqueados.remove(casa)
    if gato != [] and casa == gato[0] :
        gato.clear()
    if saida == [] :
        saida.append(casa)
        saida.append(botao) 
    else :
        saida[0] = casa
        saida[1].paint("white")
        saida[1] = botao
        saida[1].paint("blue")
        
    mostrarListas()
            
def selectBloqueio(casa, botao) :
    if gato != [] and casa == gato[0] :
        gato.clear()
    if saida != [] and casa == saida[0] :
        saida.clear()
    if casa not in bloqueados :
        bloqueados.append(casa)
    else :
        bloqueados.remove(casa)
        botao.paint("white")

    mostrarListas()

def select(component) :
    global SELECTED
    global btnSelectGato
    global btnSelectSaida
    global btnSelectGato
    
    if component == "GATO" :
        SELECTED = "GATO"
        btnSelectGato["bg"] = "orange"
        btnSelectSaida["bg"] = "white"
        btnSelectBloqueios["bg"] = "white"
        
    elif component == "SAIDA" :
        SELECTED = "SAIDA"
        btnSelectGato["bg"] = "white"
        btnSelectSaida["bg"] = "blue"
        btnSelectBloqueios["bg"] = "white"
    
    elif component == "BLOQUEIOS" :
        SELECTED = "BLOQUEIOS"
        btnSelectGato["bg"] = "white"
        btnSelectSaida["bg"] = "white"
        btnSelectBloqueios["bg"] = "red"
    
def btnSelectGato_click() :
    select("GATO")

def btnSelectSaida_click() :
    select("SAIDA")

def btnSelectBloqueios_click() :
    select("BLOQUEIOS")
        
    
# FUNCOES BOTÕES TABULEIRO
def selectCasa(casa, botao) :
    global SELECTED
    if SELECTED == "GATO" :
        selectGato(casa, botao)
    elif SELECTED == "SAIDA" :
        selectSaida(casa, botao)
    elif SELECTED == "BLOQUEIOS" :
        selectBloqueio(casa, botao)
        
# LINHA 0        
def btn00_click() :
    selectCasa((0, 0), btn00)
    
def btn01_click() :
    selectCasa((0, 1), btn01)
    
def btn02_click() :
    selectCasa((0, 2), btn02)

def btn03_click() :
    selectCasa((0, 3), btn03)
    
def btn04_click() :
    selectCasa((0, 4), btn04)

def btn05_click() :
    selectCasa((0, 5), btn05)

def btn06_click() :
    selectCasa((0, 6), btn06)

def btn07_click() :
    selectCasa((0, 7), btn07)

def btn08_click() :
    selectCasa((0, 8), btn08)

def btn09_click() :
    selectCasa((0, 9), btn09)

def btn010_click() :
    selectCasa((0, 10), btn10)

# LINHA 1        
def btn10_click() :
    selectCasa((1, 0), btn10)
              
               
# LISTAS DE INFORMAÇÕES
FirstFrame = Frame(root, width=1280, height=30)
FirstFrame.pack(side=TOP)
lblBloqueios = Label(FirstFrame, font=('calibri', 15), text="Lista de Bloqueados", width=128)
lblBloqueios.grid(row=0, column=0)

SecondFrame = Frame(root, width=1280, height=30)
SecondFrame.pack(side=TOP)          
lblGato = Label(SecondFrame, font=('calibri', 15), text="Posição do Gato", width=128)
lblGato.grid(row=0, column=0)

ThirdFrame = Frame(root, width=1280, height=30)
ThirdFrame.pack(side=TOP)
lblSaida = Label(ThirdFrame, font=('calibri', 15), text="Posição da Saída", width=128)
lblSaida.grid(row=0, column=0)


#BOTÕES DE SELEÇÃO
btnSelectGato = Button(root, width=16, text="Selecionar Gato", command=btnSelectGato_click)
btnSelectGato["cursor"] = "hand2"
btnSelectGato["bg"] = "orange"
btnSelectGato.place(x=20,y=120)

btnSelectSaida = Button(root, width=16,text="Selecionar Saída", command=btnSelectSaida_click)
btnSelectSaida["cursor"] = "hand2"
btnSelectSaida.place(x=170,y=120)

btnSelectBloqueios = Button(root, width=16,text="Selecionar Bloqueios", command=btnSelectBloqueios_click)
btnSelectBloqueios["cursor"] = "hand2"
btnSelectBloqueios.place(x=320,y=120)


# TABULEIRO
Tabuleiro = Frame(root, width=515, height=440)
Tabuleiro.pack(side=LEFT)

#BOTÕES TABULEIRO - LINHA 0
btn00 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn00_click, padding=4)
btn00["cursor"] = "hand2"
btn00.place(x=10,y=10)

btn01 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn01_click, padding=4)
btn01["cursor"] = "hand2"
btn01.place(x=55,y=10)

btn02 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn02_click, padding=4)
btn02["cursor"] = "hand2"
btn02.place(x=100,y=10)

btn03 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn03_click, padding=4)
btn03["cursor"] = "hand2"
btn03.place(x=145,y=10)

btn04 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn04_click, padding=4)
btn04["cursor"] = "hand2"
btn04.place(x=190,y=10)

btn05 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn05_click, padding=4)
btn05["cursor"] = "hand2"
btn05.place(x=235,y=10)

btn06 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn06_click, padding=4)
btn06["cursor"] = "hand2"
btn06.place(x=280,y=10)

btn07 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn07_click, padding=4)
btn07["cursor"] = "hand2"
btn07.place(x=325,y=10)

btn08 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn08_click, padding=4)
btn08["cursor"] = "hand2"
btn08.place(x=370,y=10)

btn09 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn09_click, padding=4)
btn09["cursor"] = "hand2"
btn09.place(x=415,y=10)

btn010 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn010_click, padding=4)
btn010["cursor"] = "hand2"
btn010.place(x=460,y=10)

#BOTÕES TABULEIRO - LINHA 1
btn10 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn10_click, padding=4)
btn10["cursor"] = "hand2"
btn10.place(x=32,y=53)


root.mainloop()