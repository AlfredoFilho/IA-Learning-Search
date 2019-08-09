# -*- coding: utf-8 -*-
'''
*******************Developed by********************************
    
Alfredo Albélis Batista Filho - https://github.com/AlfredoFilho
Pedro Henrique Bernini Silva - https://github.com/PedroBernini

**************************************************************** 
'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Cats.Cat_aStar import aStar
from Cats.Cat_BestFirst import bestFirst
from Cats.Cat_DepthFirst import depthFirst

gato = []
saida = []
bloqueados = []
SELECTED = "GATO"
delayGif = 200

# Colors
backgroundColor = '#2C2F33'
backgroundTabuleiroColor = '#99a6ad'
foregroundColor = 'white'
selectedColor = '#7289da'
unselectedColor = '#a1a1a3'
catSelectColor = 'orange'
blockSelectColor = 'red'
exitSelectColor = '#456fb2'
btnAlgorithmColor = '#43b581'
txtBtnColor = 'white'
catPositionColor = '#61b76b'
nodeOpenedColor = 'gray'
nodeClosedColor = 'black'
#ffe36c amarelo
#a1a1a3 cinza
#43b581 verde
#7289da azul
#faa61a laranja


# CONFIGURAÇÕES DA JANELA
root = tk.Tk()
root.geometry("1335x640+0+0")
root.resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, tk.Image('photo', file='Images/favicon.png'))
root.title("Visualização de Buscas Cegas e Heurísticas - By Alfredo Albélis; Pedro Bernini.")
root.configure(background=backgroundColor)
             
# CLASSE BOTÃO
class CustomButton(tk.Canvas) :
    def __init__(self, parent, width, height, color, command = None, padding = 4):
        tk.Canvas.__init__(self, parent, borderwidth = 0, 
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
        if SELECTED == "GATO" :
            self.paint(catSelectColor)
        elif SELECTED == "SAIDA" :
            self.paint(exitSelectColor)
        elif SELECTED == "BLOQUEIOS" :
            self.paint(blockSelectColor)
        
    def _on_release(self, event) :
        self.configure(relief="raised")
        if self.command is not None :
            self.command()

# FUNÇÕES DE SELEÇÃO
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
        gato[1].paint(catSelectColor)

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
        saida[1].paint(exitSelectColor)
            
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

def select(component) :
    global SELECTED
    global btnSelectGato
    global btnSelectSaida
    global btnSelectGato
    
    if component == "GATO" :
        SELECTED = "GATO"
        btnSelectGato["bg"] = selectedColor
        btnSelectSaida["bg"] = unselectedColor
        btnSelectBloqueios["bg"] = unselectedColor
        
    elif component == "SAIDA" :
        SELECTED = "SAIDA"
        btnSelectGato["bg"] = unselectedColor
        btnSelectSaida["bg"] = selectedColor
        btnSelectBloqueios["bg"] = unselectedColor
    
    elif component == "BLOQUEIOS" :
        SELECTED = "BLOQUEIOS"
        btnSelectGato["bg"] = unselectedColor
        btnSelectSaida["bg"] = unselectedColor
        btnSelectBloqueios["bg"] = selectedColor
    
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
    selectCasa((0, 10), btn010)

# LINHA 1        
def btn10_click() :
    selectCasa((1, 0), btn10)

def btn11_click() :
    selectCasa((1, 1), btn11)

def btn12_click() :
    selectCasa((1, 2), btn12)

def btn13_click() :
    selectCasa((1, 3), btn13)

def btn14_click() :
    selectCasa((1, 4), btn14)

def btn15_click() :
    selectCasa((1, 5), btn15)

def btn16_click() :
    selectCasa((1, 6), btn16)

def btn17_click() :
    selectCasa((1, 7), btn17)

def btn18_click() :
    selectCasa((1, 8), btn18)

def btn19_click() :
    selectCasa((1, 9), btn19)

def btn110_click() :
    selectCasa((1, 10), btn110)              

# LINHA 2        
def btn20_click() :
    selectCasa((2, 0), btn20)

def btn21_click() :
    selectCasa((2, 1), btn21)

def btn22_click() :
    selectCasa((2, 2), btn22)

def btn23_click() :
    selectCasa((2, 3), btn23)

def btn24_click() :
    selectCasa((2, 4), btn24)

def btn25_click() :
    selectCasa((2, 5), btn25)

def btn26_click() :
    selectCasa((2, 6), btn26)

def btn27_click() :
    selectCasa((2, 7), btn27)

def btn28_click() :
    selectCasa((2, 8), btn28)

def btn29_click() :
    selectCasa((2, 9), btn29)

def btn210_click() :
    selectCasa((2, 10), btn210)
    
# LINHA 3        
def btn30_click() :
    selectCasa((3, 0), btn30)

def btn31_click() :
    selectCasa((3, 1), btn31)

def btn32_click() :
    selectCasa((3, 2), btn32)

def btn33_click() :
    selectCasa((3, 3), btn33)

def btn34_click() :
    selectCasa((3, 4), btn34)

def btn35_click() :
    selectCasa((3, 5), btn35)

def btn36_click() :
    selectCasa((3, 6), btn36)

def btn37_click() :
    selectCasa((3, 7), btn37)

def btn38_click() :
    selectCasa((3, 8), btn38)

def btn39_click() :
    selectCasa((3, 9), btn39)

def btn310_click() :
    selectCasa((3, 10), btn310)
    
# LINHA 4        
def btn40_click() :
    selectCasa((4, 0), btn40)

def btn41_click() :
    selectCasa((4, 1), btn41)

def btn42_click() :
    selectCasa((4, 2), btn42)

def btn43_click() :
    selectCasa((4, 3), btn43)

def btn44_click() :
    selectCasa((4, 4), btn44)

def btn45_click() :
    selectCasa((4, 5), btn45)

def btn46_click() :
    selectCasa((4, 6), btn46)

def btn47_click() :
    selectCasa((4, 7), btn47)

def btn48_click() :
    selectCasa((4, 8), btn48)

def btn49_click() :
    selectCasa((4, 9), btn49)

def btn410_click() :
    selectCasa((4, 10), btn410)
    
# LINHA 5       
def btn50_click() :
    selectCasa((5, 0), btn50)

def btn51_click() :
    selectCasa((5, 1), btn51)

def btn52_click() :
    selectCasa((5, 2), btn52)

def btn53_click() :
    selectCasa((5, 3), btn53)

def btn54_click() :
    selectCasa((5, 4), btn54)

def btn55_click() :
    selectCasa((5, 5), btn55)

def btn56_click() :
    selectCasa((5, 6), btn56)

def btn57_click() :
    selectCasa((5, 7), btn57)

def btn58_click() :
    selectCasa((5, 8), btn58)

def btn59_click() :
    selectCasa((5, 9), btn59)

def btn510_click() :
    selectCasa((5, 10), btn510)
    
# LINHA 6       
def btn60_click() :
    selectCasa((6, 0), btn60)

def btn61_click() :
    selectCasa((6, 1), btn61)

def btn62_click() :
    selectCasa((6, 2), btn62)

def btn63_click() :
    selectCasa((6, 3), btn63)

def btn64_click() :
    selectCasa((6, 4), btn64)

def btn65_click() :
    selectCasa((6, 5), btn65)

def btn66_click() :
    selectCasa((6, 6), btn66)

def btn67_click() :
    selectCasa((6, 7), btn67)

def btn68_click() :
    selectCasa((6, 8), btn68)

def btn69_click() :
    selectCasa((6, 9), btn69)

def btn610_click() :
    selectCasa((6, 10), btn610)

# LINHA 7       
def btn70_click() :
    selectCasa((7, 0), btn70)

def btn71_click() :
    selectCasa((7, 1), btn71)

def btn72_click() :
    selectCasa((7, 2), btn72)

def btn73_click() :
    selectCasa((7, 3), btn73)

def btn74_click() :
    selectCasa((7, 4), btn74)

def btn75_click() :
    selectCasa((7, 5), btn75)

def btn76_click() :
    selectCasa((7, 6), btn76)

def btn77_click() :
    selectCasa((7, 7), btn77)

def btn78_click() :
    selectCasa((7, 8), btn78)

def btn79_click() :
    selectCasa((7, 9), btn79)

def btn710_click() :
    selectCasa((7, 10), btn710)
    
# LINHA 8       
def btn80_click() :
    selectCasa((8, 0), btn80)

def btn81_click() :
    selectCasa((8, 1), btn81)

def btn82_click() :
    selectCasa((8, 2), btn82)

def btn83_click() :
    selectCasa((8, 3), btn83)

def btn84_click() :
    selectCasa((8, 4), btn84)

def btn85_click() :
    selectCasa((8, 5), btn85)

def btn86_click() :
    selectCasa((8, 6), btn86)

def btn87_click() :
    selectCasa((8, 7), btn87)

def btn88_click() :
    selectCasa((8, 8), btn88)

def btn89_click() :
    selectCasa((8, 9), btn89)

def btn810_click() :
    selectCasa((8, 10), btn810)
    
# LINHA 9       
def btn90_click() :
    selectCasa((9, 0), btn90)

def btn91_click() :
    selectCasa((9, 1), btn91)

def btn92_click() :
    selectCasa((9, 2), btn92)

def btn93_click() :
    selectCasa((9, 3), btn93)

def btn94_click() :
    selectCasa((9, 4), btn94)

def btn95_click() :
    selectCasa((9, 5), btn95)

def btn96_click() :
    selectCasa((9, 6), btn96)

def btn97_click() :
    selectCasa((9, 7), btn97)

def btn98_click() :
    selectCasa((9, 8), btn98)

def btn99_click() :
    selectCasa((9, 9), btn99)

def btn910_click() :
    selectCasa((9, 10), btn910)
    
# LINHA 9       
def btn100_click() :
    selectCasa((10, 0), btn100)

def btn101_click() :
    selectCasa((10, 1), btn101)

def btn102_click() :
    selectCasa((10, 2), btn102)

def btn103_click() :
    selectCasa((10, 3), btn103)

def btn104_click() :
    selectCasa((10, 4), btn104)

def btn105_click() :
    selectCasa((10, 5), btn105)

def btn106_click() :
    selectCasa((10, 6), btn106)

def btn107_click() :
    selectCasa((10, 7), btn107)

def btn108_click() :
    selectCasa((10, 8), btn108)

def btn109_click() :
    selectCasa((10, 9), btn109)

def btn1010_click() :
    selectCasa((10, 10), btn1010)
    
    
# FUNCOES BOTÕES ALGORITMOS
def existeVazio() :
    if gato == [] and saida != [] :
        gatoVazio()
        return True
    elif gato != [] and saida == [] :
        saidaVazio()
        return True
    elif gato == [] and saida == [] :
        ambosVazio()
        return True
    else :
        return False
        
def gatoVazio() :
    messagebox.showinfo("Parâmetros de busca", "Para realizar a busca, escolha uma posição para o gato.")

def saidaVazio() :
    messagebox.showinfo("Parâmetros de busca", "Para realizar a busca, escolha uma posição para a saída.")
    
def ambosVazio() :
    messagebox.showinfo("Parâmetros de busca", "Para realizar a busca, escolha uma posição para o gato e para saída.")

def btnAstar_click() :
    if existeVazio() is not True:
        aStar(gato[0], saida[0], bloqueados, delayGif)
        print("Busca A*")
    
def btnBestFirst_click() :
    if existeVazio() is not True:
        bestFirst(gato[0], saida[0], bloqueados, delayGif)
        print("Busca Best-First")
    
def btnAmplitude_click() :
    if existeVazio() is not True:
        print("Busca em Amplitude")
    
def btnProfundidade_click() :
    if existeVazio() is not True:
        depthFirst(gato[0], saida[0], bloqueados, delayGif)
        print("Busca em Profundidade")
        
# FUNÇÕES DE DELAY
def paintBtnDelay(botao):
    global btnMtLento
    global btnLento
    global btnNormal
    global btnRapido
    global btnMtRapido
    
    btnMtLento["bg"] = unselectedColor
    btnLento["bg"] = unselectedColor
    btnNormal["bg"] = unselectedColor
    btnRapido["bg"] = unselectedColor
    btnMtRapido["bg"] = unselectedColor
    
    if botao == "Muito Lento":
        btnMtLento["bg"] = selectedColor
    elif botao == "Lento":
        btnLento["bg"] = selectedColor
    elif botao == "Normal":
        btnNormal["bg"] = selectedColor
    elif botao == "Rapido":
        btnRapido["bg"] = selectedColor
    elif botao == "Muito Rapido":
        btnMtRapido["bg"] = selectedColor
    
def setDelayGif(delay):
    global delayGif
    delayGif = delay
    
def btnMtLento_Click():
    setDelayGif(400)
    paintBtnDelay("Muito Lento")
    
def btnLento_Click():
    setDelayGif(240)
    paintBtnDelay("Lento")

def btnNormal_Click():
    setDelayGif(160)
    paintBtnDelay("Normal")

def btnRapido_Click():
    setDelayGif(80)
    paintBtnDelay("Rapido")

def btnMtRapido_Click():
    setDelayGif(40)
    paintBtnDelay("Muito Rapido")
    
    
# FRAME DE SELEÇÃO
frameSelection = tk.LabelFrame(root, text="Seleção de Parâmetros", borderwidth=2, foreground=foregroundColor,relief=tk.RAISED, bg=backgroundColor, width=500, height=75, padx=20, pady=15)
frameSelection.place(x=40, y=20)

#BOTÕES DE SELEÇÃO
btnSelectGato = tk.Button(frameSelection, width=16, text="Selecionar Gato", foreground=txtBtnColor, command=btnSelectGato_click)
btnSelectGato["cursor"] = "hand2"
btnSelectGato["bg"] = selectedColor
btnSelectGato.place(x=0,y=0)

btnSelectSaida = tk.Button(frameSelection, width=16,text="Selecionar Saída", foreground=txtBtnColor, command=btnSelectSaida_click)
btnSelectSaida["cursor"] = "hand2"
btnSelectSaida["bg"] = unselectedColor
btnSelectSaida.place(x=170,y=0)

btnSelectBloqueios = tk.Button(frameSelection, width=16,text="Selecionar Bloqueios", foreground=txtBtnColor, command=btnSelectBloqueios_click)
btnSelectBloqueios["cursor"] = "hand2"
btnSelectBloqueios["bg"] = unselectedColor
btnSelectBloqueios.place(x=340,y=0)


# FRAME DE TABULEIRO
frameTabuleiro = tk.LabelFrame(root, text="Tabuleiro", borderwidth=2, foreground=foregroundColor, relief=tk.RAISED, bg=backgroundColor, width=540, height=512)
frameTabuleiro.place(x=20, y=100)

# TABULEIRO
Tabuleiro = tk.Frame(frameTabuleiro, bg=backgroundTabuleiroColor, width=537, height=493)
Tabuleiro.place(x=-1, y=0)

#BOTÕES TABULEIRO - LINHA 0
btn00 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn00_click, padding=4)
btn00["cursor"] = "hand2"
btn00["bg"] = backgroundTabuleiroColor
btn00.place(x=10,y=10)

btn01 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn01_click, padding=4)
btn01["cursor"] = "hand2"
btn01["bg"] = backgroundTabuleiroColor
btn01.place(x=55,y=10)

btn02 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn02_click, padding=4)
btn02["cursor"] = "hand2"
btn02["bg"] = backgroundTabuleiroColor
btn02.place(x=100,y=10)

btn03 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn03_click, padding=4)
btn03["cursor"] = "hand2"
btn03["bg"] = backgroundTabuleiroColor
btn03.place(x=145,y=10)

btn04 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn04_click, padding=4)
btn04["cursor"] = "hand2"
btn04["bg"] = backgroundTabuleiroColor
btn04.place(x=190,y=10)

btn05 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn05_click, padding=4)
btn05["cursor"] = "hand2"
btn05["bg"] = backgroundTabuleiroColor
btn05.place(x=235,y=10)

btn06 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn06_click, padding=4)
btn06["cursor"] = "hand2"
btn06["bg"] = backgroundTabuleiroColor
btn06.place(x=280,y=10)

btn07 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn07_click, padding=4)
btn07["cursor"] = "hand2"
btn07["bg"] = backgroundTabuleiroColor
btn07.place(x=325,y=10)

btn08 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn08_click, padding=4)
btn08["cursor"] = "hand2"
btn08["bg"] = backgroundTabuleiroColor
btn08.place(x=370,y=10)

btn09 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn09_click, padding=4)
btn09["cursor"] = "hand2"
btn09["bg"] = backgroundTabuleiroColor
btn09.place(x=415,y=10)

btn010 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn010_click, padding=4)
btn010["cursor"] = "hand2"
btn010["bg"] = backgroundTabuleiroColor
btn010.place(x=460,y=10)

#BOTÕES TABULEIRO - LINHA 1
btn10 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn10_click, padding=4)
btn10["cursor"] = "hand2"
btn10["bg"] = backgroundTabuleiroColor
btn10.place(x=32,y=53)

btn11 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn11_click, padding=4)
btn11["cursor"] = "hand2"
btn11["bg"] = backgroundTabuleiroColor
btn11.place(x=77,y=53)

btn12 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn12_click, padding=4)
btn12["cursor"] = "hand2"
btn12["bg"] = backgroundTabuleiroColor
btn12.place(x=122,y=53)

btn13 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn13_click, padding=4)
btn13["cursor"] = "hand2"
btn13["bg"] = backgroundTabuleiroColor
btn13.place(x=167,y=53)

btn14 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn14_click, padding=4)
btn14["cursor"] = "hand2"
btn14["bg"] = backgroundTabuleiroColor
btn14.place(x=212,y=53)

btn15 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn15_click, padding=4)
btn15["cursor"] = "hand2"
btn15["bg"] = backgroundTabuleiroColor
btn15.place(x=257,y=53)

btn16 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn16_click, padding=4)
btn16["cursor"] = "hand2"
btn16["bg"] = backgroundTabuleiroColor
btn16.place(x=302,y=53)

btn17 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn17_click, padding=4)
btn17["cursor"] = "hand2"
btn17["bg"] = backgroundTabuleiroColor
btn17.place(x=347,y=53)

btn18 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn18_click, padding=4)
btn18["cursor"] = "hand2"
btn18["bg"] = backgroundTabuleiroColor
btn18.place(x=392,y=53)

btn19 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn19_click, padding=4)
btn19["cursor"] = "hand2"
btn19["bg"] = backgroundTabuleiroColor
btn19.place(x=437,y=53)

btn110 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn110_click, padding=4)
btn110["cursor"] = "hand2"
btn110["bg"] = backgroundTabuleiroColor
btn110.place(x=482,y=53)

#BOTÕES TABULEIRO - LINHA 2
btn20 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn20_click, padding=4)
btn20["cursor"] = "hand2"
btn20["bg"] = backgroundTabuleiroColor
btn20.place(x=10,y=96)

btn21 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn21_click, padding=4)
btn21["cursor"] = "hand2"
btn21["bg"] = backgroundTabuleiroColor
btn21.place(x=55,y=96)

btn22 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn22_click, padding=4)
btn22["cursor"] = "hand2"
btn22["bg"] = backgroundTabuleiroColor
btn22.place(x=100,y=96)

btn23 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn23_click, padding=4)
btn23["cursor"] = "hand2"
btn23["bg"] = backgroundTabuleiroColor
btn23.place(x=145,y=96)

btn24 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn24_click, padding=4)
btn24["cursor"] = "hand2"
btn24["bg"] = backgroundTabuleiroColor
btn24.place(x=190,y=96)

btn25 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn25_click, padding=4)
btn25["cursor"] = "hand2"
btn25["bg"] = backgroundTabuleiroColor
btn25.place(x=235,y=96)

btn26 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn26_click, padding=4)
btn26["cursor"] = "hand2"
btn26["bg"] = backgroundTabuleiroColor
btn26.place(x=280,y=96)

btn27 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn27_click, padding=4)
btn27["cursor"] = "hand2"
btn27["bg"] = backgroundTabuleiroColor
btn27.place(x=325,y=96)

btn28 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn28_click, padding=4)
btn28["cursor"] = "hand2"
btn28["bg"] = backgroundTabuleiroColor
btn28.place(x=370,y=96)

btn29 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn29_click, padding=4)
btn29["cursor"] = "hand2"
btn29["bg"] = backgroundTabuleiroColor
btn29.place(x=415,y=96)

btn210 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn210_click, padding=4)
btn210["cursor"] = "hand2"
btn210["bg"] = backgroundTabuleiroColor
btn210.place(x=460,y=96)

#BOTÕES TABULEIRO - LINHA 3
btn30 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn30_click, padding=4)
btn30["cursor"] = "hand2"
btn30["bg"] = backgroundTabuleiroColor
btn30.place(x=32,y=139)

btn31 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn31_click, padding=4)
btn31["cursor"] = "hand2"
btn31["bg"] = backgroundTabuleiroColor
btn31.place(x=77,y=139)

btn32 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn32_click, padding=4)
btn32["cursor"] = "hand2"
btn32["bg"] = backgroundTabuleiroColor
btn32.place(x=122,y=139)

btn33 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn33_click, padding=4)
btn33["cursor"] = "hand2"
btn33["bg"] = backgroundTabuleiroColor
btn33.place(x=167,y=139)

btn34 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn34_click, padding=4)
btn34["cursor"] = "hand2"
btn34["bg"] = backgroundTabuleiroColor
btn34.place(x=212,y=139)

btn35 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn35_click, padding=4)
btn35["cursor"] = "hand2"
btn35["bg"] = backgroundTabuleiroColor
btn35.place(x=257,y=139)

btn36 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn36_click, padding=4)
btn36["cursor"] = "hand2"
btn36["bg"] = backgroundTabuleiroColor
btn36.place(x=302,y=139)

btn37 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn37_click, padding=4)
btn37["cursor"] = "hand2"
btn37["bg"] = backgroundTabuleiroColor
btn37.place(x=347,y=139)

btn38 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn38_click, padding=4)
btn38["cursor"] = "hand2"
btn38["bg"] = backgroundTabuleiroColor
btn38.place(x=392,y=139)

btn39 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn39_click, padding=4)
btn39["cursor"] = "hand2"
btn39["bg"] = backgroundTabuleiroColor
btn39.place(x=437,y=139)

btn310 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn310_click, padding=4)
btn310["cursor"] = "hand2"
btn310["bg"] = backgroundTabuleiroColor
btn310.place(x=482,y=139)

#BOTÕES TABULEIRO - LINHA 4
btn40 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn40_click, padding=4)
btn40["cursor"] = "hand2"
btn40["bg"] = backgroundTabuleiroColor
btn40.place(x=10,y=182)

btn41 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn41_click, padding=4)
btn41["cursor"] = "hand2"
btn41["bg"] = backgroundTabuleiroColor
btn41.place(x=55,y=182)

btn42 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn42_click, padding=4)
btn42["cursor"] = "hand2"
btn42["bg"] = backgroundTabuleiroColor
btn42.place(x=100,y=182)

btn43 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn43_click, padding=4)
btn43["cursor"] = "hand2"
btn43["bg"] = backgroundTabuleiroColor
btn43.place(x=145,y=182)

btn44 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn44_click, padding=4)
btn44["cursor"] = "hand2"
btn44["bg"] = backgroundTabuleiroColor
btn44.place(x=190,y=182)

btn45 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn45_click, padding=4)
btn45["cursor"] = "hand2"
btn45["bg"] = backgroundTabuleiroColor
btn45.place(x=235,y=182)

btn46 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn46_click, padding=4)
btn46["cursor"] = "hand2"
btn46["bg"] = backgroundTabuleiroColor
btn46.place(x=280,y=182)

btn47 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn47_click, padding=4)
btn47["cursor"] = "hand2"
btn47["bg"] = backgroundTabuleiroColor
btn47.place(x=325,y=182)

btn48 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn48_click, padding=4)
btn48["cursor"] = "hand2"
btn48["bg"] = backgroundTabuleiroColor
btn48.place(x=370,y=182)

btn49 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn49_click, padding=4)
btn49["cursor"] = "hand2"
btn49["bg"] = backgroundTabuleiroColor
btn49.place(x=415,y=182)

btn410 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn410_click, padding=4)
btn410["cursor"] = "hand2"
btn410["bg"] = backgroundTabuleiroColor
btn410.place(x=460,y=182)

#BOTÕES TABULEIRO - LINHA 5
btn50 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn50_click, padding=4)
btn50["cursor"] = "hand2"
btn50["bg"] = backgroundTabuleiroColor
btn50.place(x=32,y=225)

btn51 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn51_click, padding=4)
btn51["cursor"] = "hand2"
btn51["bg"] = backgroundTabuleiroColor
btn51.place(x=77,y=225)

btn52 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn52_click, padding=4)
btn52["cursor"] = "hand2"
btn52["bg"] = backgroundTabuleiroColor
btn52.place(x=122,y=225)

btn53 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn53_click, padding=4)
btn53["cursor"] = "hand2"
btn53["bg"] = backgroundTabuleiroColor
btn53.place(x=167,y=225)

btn54 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn54_click, padding=4)
btn54["cursor"] = "hand2"
btn54["bg"] = backgroundTabuleiroColor
btn54.place(x=212,y=225)

btn55 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn55_click, padding=4)
btn55["cursor"] = "hand2"
btn55["bg"] = backgroundTabuleiroColor
btn55.place(x=257,y=225)

btn56 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn56_click, padding=4)
btn56["cursor"] = "hand2"
btn56["bg"] = backgroundTabuleiroColor
btn56.place(x=302,y=225)

btn57 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn57_click, padding=4)
btn57["cursor"] = "hand2"
btn57["bg"] = backgroundTabuleiroColor
btn57.place(x=347,y=225)

btn58 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn58_click, padding=4)
btn58["cursor"] = "hand2"
btn58["bg"] = backgroundTabuleiroColor
btn58.place(x=392,y=225)

btn59 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn59_click, padding=4)
btn59["cursor"] = "hand2"
btn59["bg"] = backgroundTabuleiroColor
btn59.place(x=437,y=225)

btn510 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn510_click, padding=4)
btn510["cursor"] = "hand2"
btn510["bg"] = backgroundTabuleiroColor
btn510.place(x=482,y=225)

#BOTÕES TABULEIRO - LINHA 6
btn60 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn60_click, padding=4)
btn60["cursor"] = "hand2"
btn60["bg"] = backgroundTabuleiroColor
btn60.place(x=10,y=268)

btn61 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn61_click, padding=4)
btn61["cursor"] = "hand2"
btn61["bg"] = backgroundTabuleiroColor
btn61.place(x=55,y=268)

btn62 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn62_click, padding=4)
btn62["cursor"] = "hand2"
btn62["bg"] = backgroundTabuleiroColor
btn62.place(x=100,y=268)

btn63 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn63_click, padding=4)
btn63["cursor"] = "hand2"
btn63["bg"] = backgroundTabuleiroColor
btn63.place(x=145,y=268)

btn64 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn64_click, padding=4)
btn64["cursor"] = "hand2"
btn64["bg"] = backgroundTabuleiroColor
btn64.place(x=190,y=268)

btn65 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn65_click, padding=4)
btn65["cursor"] = "hand2"
btn65["bg"] = backgroundTabuleiroColor
btn65.place(x=235,y=268)

btn66 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn66_click, padding=4)
btn66["cursor"] = "hand2"
btn66["bg"] = backgroundTabuleiroColor
btn66.place(x=280,y=268)

btn67 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn67_click, padding=4)
btn67["cursor"] = "hand2"
btn67["bg"] = backgroundTabuleiroColor
btn67.place(x=325,y=268)

btn68 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn68_click, padding=4)
btn68["cursor"] = "hand2"
btn68["bg"] = backgroundTabuleiroColor
btn68.place(x=370,y=268)

btn69 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn69_click, padding=4)
btn69["cursor"] = "hand2"
btn69["bg"] = backgroundTabuleiroColor
btn69.place(x=415,y=268)

btn610 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn610_click, padding=4)
btn610["cursor"] = "hand2"
btn610["bg"] = backgroundTabuleiroColor
btn610.place(x=460,y=268)

#BOTÕES TABULEIRO - LINHA 7
btn70 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn70_click, padding=4)
btn70["cursor"] = "hand2"
btn70["bg"] = backgroundTabuleiroColor
btn70.place(x=32,y=311)

btn71 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn71_click, padding=4)
btn71["cursor"] = "hand2"
btn71["bg"] = backgroundTabuleiroColor
btn71.place(x=77,y=311)

btn72 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn72_click, padding=4)
btn72["cursor"] = "hand2"
btn72["bg"] = backgroundTabuleiroColor
btn72.place(x=122,y=311)

btn73 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn73_click, padding=4)
btn73["cursor"] = "hand2"
btn73["bg"] = backgroundTabuleiroColor
btn73.place(x=167,y=311)

btn74 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn74_click, padding=4)
btn74["cursor"] = "hand2"
btn74["bg"] = backgroundTabuleiroColor
btn74.place(x=212,y=311)

btn75 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn75_click, padding=4)
btn75["cursor"] = "hand2"
btn75["bg"] = backgroundTabuleiroColor
btn75.place(x=257,y=311)

btn76 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn76_click, padding=4)
btn76["cursor"] = "hand2"
btn76["bg"] = backgroundTabuleiroColor
btn76.place(x=302,y=311)

btn77 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn77_click, padding=4)
btn77["cursor"] = "hand2"
btn77["bg"] = backgroundTabuleiroColor
btn77.place(x=347,y=311)

btn78 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn78_click, padding=4)
btn78["cursor"] = "hand2"
btn78["bg"] = backgroundTabuleiroColor
btn78.place(x=392,y=311)

btn79 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn79_click, padding=4)
btn79["cursor"] = "hand2"
btn79["bg"] = backgroundTabuleiroColor
btn79.place(x=437,y=311)

btn710 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn710_click, padding=4)
btn710["cursor"] = "hand2"
btn710["bg"] = backgroundTabuleiroColor
btn710.place(x=482,y=311)

#BOTÕES TABULEIRO - LINHA 8
btn80 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn80_click, padding=4)
btn80["cursor"] = "hand2"
btn80["bg"] = backgroundTabuleiroColor
btn80.place(x=10,y=354)

btn81 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn81_click, padding=4)
btn81["cursor"] = "hand2"
btn81["bg"] = backgroundTabuleiroColor
btn81.place(x=55,y=354)

btn82 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn82_click, padding=4)
btn82["cursor"] = "hand2"
btn82["bg"] = backgroundTabuleiroColor
btn82.place(x=100,y=354)

btn83 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn83_click, padding=4)
btn83["cursor"] = "hand2"
btn83["bg"] = backgroundTabuleiroColor
btn83.place(x=145,y=354)

btn84 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn84_click, padding=4)
btn84["cursor"] = "hand2"
btn84["bg"] = backgroundTabuleiroColor
btn84.place(x=190,y=354)

btn85 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn85_click, padding=4)
btn85["cursor"] = "hand2"
btn85["bg"] = backgroundTabuleiroColor
btn85.place(x=235,y=354)

btn86 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn86_click, padding=4)
btn86["cursor"] = "hand2"
btn86["bg"] = backgroundTabuleiroColor
btn86.place(x=280,y=354)

btn87 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn87_click, padding=4)
btn87["cursor"] = "hand2"
btn87["bg"] = backgroundTabuleiroColor
btn87.place(x=325,y=354)

btn88 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn88_click, padding=4)
btn88["cursor"] = "hand2"
btn88["bg"] = backgroundTabuleiroColor
btn88.place(x=370,y=354)

btn89 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn89_click, padding=4)
btn89["cursor"] = "hand2"
btn89["bg"] = backgroundTabuleiroColor
btn89.place(x=415,y=354)

btn810 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn810_click, padding=4)
btn810["cursor"] = "hand2"
btn810["bg"] = backgroundTabuleiroColor
btn810.place(x=460,y=354)

#BOTÕES TABULEIRO - LINHA 9
btn90 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn90_click, padding=4)
btn90["cursor"] = "hand2"
btn90["bg"] = backgroundTabuleiroColor
btn90.place(x=32,y=397)

btn91 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn91_click, padding=4)
btn91["cursor"] = "hand2"
btn91["bg"] = backgroundTabuleiroColor
btn91.place(x=77,y=397)

btn92 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn92_click, padding=4)
btn92["cursor"] = "hand2"
btn92["bg"] = backgroundTabuleiroColor
btn92.place(x=122,y=397)

btn93 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn93_click, padding=4)
btn93["cursor"] = "hand2"
btn93["bg"] = backgroundTabuleiroColor
btn93.place(x=167,y=397)

btn94 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn94_click, padding=4)
btn94["cursor"] = "hand2"
btn94["bg"] = backgroundTabuleiroColor
btn94.place(x=212,y=397)

btn95 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn95_click, padding=4)
btn95["cursor"] = "hand2"
btn95["bg"] = backgroundTabuleiroColor
btn95.place(x=257,y=397)

btn96 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn96_click, padding=4)
btn96["cursor"] = "hand2"
btn96["bg"] = backgroundTabuleiroColor
btn96.place(x=302,y=397)

btn97 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn97_click, padding=4)
btn97["cursor"] = "hand2"
btn97["bg"] = backgroundTabuleiroColor
btn97.place(x=347,y=397)

btn98 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn98_click, padding=4)
btn98["cursor"] = "hand2"
btn98["bg"] = backgroundTabuleiroColor
btn98.place(x=392,y=397)

btn99 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn99_click, padding=4)
btn99["cursor"] = "hand2"
btn99["bg"] = backgroundTabuleiroColor
btn99.place(x=437,y=397)

btn910 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn910_click, padding=4)
btn910["cursor"] = "hand2"
btn910["bg"] = backgroundTabuleiroColor
btn910.place(x=482,y=397)

#BOTÕES TABULEIRO - LINHA 10
btn100 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn100_click, padding=4)
btn100["cursor"] = "hand2"
btn100["bg"] = backgroundTabuleiroColor
btn100.place(x=10,y=440)

btn101 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn101_click, padding=4)
btn101["cursor"] = "hand2"
btn101["bg"] = backgroundTabuleiroColor
btn101.place(x=55,y=440)

btn102 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn102_click, padding=4)
btn102["cursor"] = "hand2"
btn102["bg"] = backgroundTabuleiroColor
btn102.place(x=100,y=440)

btn103 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn103_click, padding=4)
btn103["cursor"] = "hand2"
btn103["bg"] = backgroundTabuleiroColor
btn103.place(x=145,y=440)

btn104 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn104_click, padding=4)
btn104["cursor"] = "hand2"
btn104["bg"] = backgroundTabuleiroColor
btn104.place(x=190,y=440)

btn105 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn105_click, padding=4)
btn105["cursor"] = "hand2"
btn105["bg"] = backgroundTabuleiroColor
btn105.place(x=235,y=440)

btn106 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn106_click, padding=4)
btn106["cursor"] = "hand2"
btn106["bg"] = backgroundTabuleiroColor
btn106.place(x=280,y=440)

btn107 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn107_click, padding=4)
btn107["cursor"] = "hand2"
btn107["bg"] = backgroundTabuleiroColor
btn107.place(x=325,y=440)

btn108 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn108_click, padding=4)
btn108["cursor"] = "hand2"
btn108["bg"] = backgroundTabuleiroColor
btn108.place(x=370,y=440)

btn109 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn109_click, padding=4)
btn109["cursor"] = "hand2"
btn109["bg"] = backgroundTabuleiroColor
btn109.place(x=415,y=440)

btn1010 = CustomButton(Tabuleiro, width=35, height=35, color="white", command=btn1010_click, padding=4)
btn1010["cursor"] = "hand2"
btn1010["bg"] = backgroundTabuleiroColor
btn1010.place(x=460,y=440)


# FRAME DOS ALGORITMOS
frameAlgorithm = tk.LabelFrame(root, text="Realizar Busca", borderwidth=2, foreground=foregroundColor,relief=RAISED, bg=backgroundColor, width=572, height=170, padx=20, pady=15)
frameAlgorithm.place(x=650, y=350)

# BOTÕES DOS ALGORITMOS
btnAstar = tk.Button(frameAlgorithm, width=20, height=1, font=('calibri', 16), text="A*", foreground=txtBtnColor, command=btnAstar_click)
btnAstar["cursor"] = "hand2"
btnAstar["bg"] = btnAlgorithmColor
btnAstar.place(x=0,y=0)

btnBestFirst = tk.Button(frameAlgorithm, width=20, height=1, font=('calibri', 16), text="Melhor-Primeiro", foreground=txtBtnColor, command=btnBestFirst_click)
btnBestFirst["cursor"] = "hand2"
btnBestFirst["bg"] = btnAlgorithmColor
btnBestFirst.place(x=300,y=0)

btnAmplitude = tk.Button(frameAlgorithm, width=20, height=1, font=('calibri', 16), text="Amplitude", foreground=txtBtnColor, command=btnAmplitude_click)
btnAmplitude["cursor"] = "hand2"
btnAmplitude["bg"] = btnAlgorithmColor
btnAmplitude.place(x=0,y=70)

btnProfundidade = tk.Button(frameAlgorithm, width=20, height=1, font=('calibri', 16), text="Profundidade", foreground=txtBtnColor, command=btnProfundidade_click)
btnProfundidade["cursor"] = "hand2"
btnProfundidade["bg"] = btnAlgorithmColor
btnProfundidade.place(x=300,y=70)


# FRAME DO DELAY
frameDelay = tk.LabelFrame(root, text="Velocidade da Animação", borderwidth=2, foreground=foregroundColor, relief=tk.RAISED, bg=backgroundColor, width=716, height=75, padx=20, pady=15)
frameDelay.place(x=590, y=536)
  
# BOTÕES DE DELAY
btnMtLento = tk.Button(frameDelay, width=15, text="Muito Lenta", foreground=txtBtnColor, command=btnMtLento_Click)
btnMtLento["cursor"] = "hand2"
btnMtLento["bg"] = unselectedColor
btnMtLento.place(x=0,y=0)

btnLento = tk.Button(frameDelay, width=15, text="Lenta", foreground=txtBtnColor, command=btnLento_Click)
btnLento["cursor"] = "hand2"
btnLento["bg"] = unselectedColor
btnLento.place(x=140,y=0)

btnNormal = tk.Button(frameDelay, width=15, text="Normal", foreground=txtBtnColor, command=btnNormal_Click)
btnNormal["cursor"] = "hand2"
btnNormal["bg"] = selectedColor
btnNormal.place(x=280,y=0)

btnRapido = tk.Button(frameDelay, width=15, text="Rápida", foreground=txtBtnColor, command=btnRapido_Click)
btnRapido["cursor"] = "hand2"
btnRapido["bg"] = unselectedColor
btnRapido.place(x=420,y=0)

btnMtRapido = tk.Button(frameDelay, width=15, text="Muito Rápida", foreground=txtBtnColor, command=btnMtRapido_Click)
btnMtRapido["cursor"] = "hand2"
btnMtRapido["bg"] = unselectedColor
btnMtRapido.place(x=560,y=0)


# FRAME DE LEGENDAS
frameLegenda = tk.LabelFrame(root, text="Legendas:", borderwidth=0, foreground=foregroundColor, relief=tk.RIDGE, bg=backgroundColor, width=400, height=325, padx=20, pady=15)
frameLegenda.place(x=650, y=20)

# LEGENDAS
frameInicio = tk.Frame(frameLegenda, width=350, height=35, bg=backgroundColor)
frameInicio.place(x=0, y=0)
corInicio = tk.Frame(frameInicio, width=25, height=25, bg=catSelectColor)
corInicio.place(x=5,y=5)
legendaInicio = tk.Label(frameInicio, foreground="white", bg=backgroundColor, text="Posição inicial do Gato")
legendaInicio.place(x=34, y=7)

frameNoAberto = tk.Frame(frameLegenda, width=350, height=35, bg=backgroundColor)
frameNoAberto.place(x=0, y=40)
corNoAberto = tk.Frame(frameNoAberto, width=25, height=25, bg=nodeOpenedColor)
corNoAberto.place(x=5,y=5)
legendaNoAberto = tk.Label(frameNoAberto, foreground="white", bg=backgroundColor, text="Nós Abertos")
legendaNoAberto.place(x=34, y=7)

frameNoFechado = tk.Frame(frameLegenda, width=350, height=35, bg=backgroundColor)
frameNoFechado.place(x=0, y=80)
corNoFechado = tk.Frame(frameNoFechado, width=25, height=25, bg=nodeClosedColor)
corNoFechado.place(x=5,y=5)
legendaNoFechado = tk.Label(frameNoFechado, foreground="white", bg=backgroundColor, text="Nós Fechados")
legendaNoFechado.place(x=34, y=7)

framePosicaoGato = tk.Frame(frameLegenda, width=350, height=35, bg=backgroundColor)
framePosicaoGato.place(x=0, y=120)
corPosicaoGato = tk.Frame(framePosicaoGato, width=25, height=25, bg=catPositionColor)
corPosicaoGato.place(x=5,y=5)
legendaPosicaoGato = tk.Label(framePosicaoGato, foreground="white", bg=backgroundColor, text="Posição Atual do Gato")
legendaPosicaoGato.place(x=34, y=7)

frameBacktracking = tk.Frame(frameLegenda, width=350, height=35, bg=backgroundColor)
frameBacktracking.place(x=0, y=160)
corBacktracking = tk.Frame(frameBacktracking, width=25, height=25, bg=catPositionColor)
corBacktracking.place(x=5,y=5)
letra = tk.Label(corBacktracking, foreground="black", bg=catPositionColor, text="B")
letra.place(x=6,y=3)
legendaBacktracking = tk.Label(frameBacktracking, foreground="white", bg=backgroundColor, text="Caminho de Backtracking")
legendaBacktracking.place(x=34, y=7)

frameBloqueio = tk.Frame(frameLegenda, width=350, height=35, bg=backgroundColor)
frameBloqueio.place(x=0, y=200)
corBloqueio = tk.Frame(frameBloqueio, width=25, height=25, bg=blockSelectColor)
corBloqueio.place(x=5,y=5)
legendaBloqueio = tk.Label(frameBloqueio, foreground="white", bg=backgroundColor, text="Bloqueio")
legendaBloqueio.place(x=34, y=7)

frameSaida = tk.Frame(frameLegenda, width=350, height=35, bg=backgroundColor)
frameSaida.place(x=0, y=240)
corSaida = tk.Frame(frameSaida, width=25, height=25, bg=exitSelectColor)
corSaida.place(x=5,y=5)
legendaSaida = tk.Label(frameSaida, foreground="white", bg=backgroundColor, text="Saída")
legendaSaida.place(x=34, y=7)


root.mainloop()





