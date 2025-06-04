import tkinter as tk
from threading import Thread
from tkinter import messagebox
from Cats.Cat_aStar import aStar
from Cats.Cat_BestFirst import bestFirst
from Cats.Cat_DepthFirst import depthFirst
from Cats.Cat_BreadthFirstSearch import breadthFirstSearch
from GifMaker.GifShow import Gif

import webbrowser  # No início do arquivo, se ainda não estiver


# Cores e configurações
BACKGROUND_COLOR = '#2C2F33'
TABULEIRO_BG_COLOR = '#597e8d'
TXT_BTN_COLOR = 'white'
COLOR_SELECTED = '#7289da'
COLOR_UNSELECTED = '#a1a1a3'
COLOR_CAT = 'orange'
COLOR_OPEN_NODE = 'gray'
COLOR_CLOSED_NODE = 'black'
COLOR_BLOCK = 'red'
COLOR_EXIT = '#456fb2'
DELAY_MAP = {
    'Muito Lenta': 1000,
    'Lenta': 500,
    'Normal': 200,
    'Rápida': 100,
    'Muito Rápida': 30
}

# Estado global
gato = []
saida = []
bloqueados = []
SELECTED = "GATO"
delayGif = DELAY_MAP['Normal']

# Canvas tabuleiro quadrado responsivo
import tkinter as tk

class TabuleiroCanvas(tk.Canvas):
    def __init__(self, master, linhas=11, colunas=11, **kwargs):
        super().__init__(master, **kwargs)
        self.linhas = linhas
        self.colunas = colunas
        self.celulas = []  # IDs dos retângulos
        self.bind("<Configure>", self.redesenhar)
        self.bind("<Button-1>", self.click_celula)

    def redesenhar(self, event=None):
        self.delete("all")
        largura = self.winfo_width()
        altura = self.winfo_height()
        
        tam_celula = min(
            largura / (self.colunas + 0.5),
            altura / self.linhas
        )
        
        x0 = (largura - (tam_celula * self.colunas + tam_celula / 2)) / 2
        y0 = (altura - tam_celula * self.linhas) / 2

        margem = tam_celula * 0.02  # espaço entre círculos
        
        self.tam_celula = tam_celula
        self.x0 = x0
        self.y0 = y0

        self.celulas = []
        for i in range(self.linhas):
            linha = []
            offset_x = tam_celula / 2 if i % 2 == 1 else 0
            for j in range(self.colunas):
                x1 = x0 + j * tam_celula + offset_x + margem
                y1 = y0 + i * tam_celula + margem
                x2 = x0 + j * tam_celula + offset_x + tam_celula - margem
                y2 = y0 + i * tam_celula + tam_celula - margem
                ret = self.create_oval(
                    x1, y1, x2, y2,
                    fill='white',
                    outline='#555555',  # cinza escuro para a borda
                    width=2  # largura da borda maior
                )
                
                # Adiciona o texto no centro do círculo
                cx = (x1 + x2) / 2
                cy = (y1 + y2) / 2
                self.create_text(cx, cy, text=f"{i},{j}", fill="black", font=("Arial", int(tam_celula*0.25)))
                
                linha.append(ret)
            self.celulas.append(linha)
        self.atualizar_cores()

    def click_celula(self, event):
        cx, cy = event.x, event.y
        i = int((cy - self.y0) / self.tam_celula)
        if i < 0 or i >= self.linhas:
            return
        
        offset_x = self.tam_celula / 2 if i % 2 == 1 else 0
        j = int((cx - self.x0 - offset_x) / self.tam_celula)
        if 0 <= j < self.colunas:
            select((i, j))

    def atualizar_cores(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                cell = (i, j)
                cor = 'white'
                if gato and cell == gato[0]:
                    cor = COLOR_CAT
                elif saida and cell == saida[0]:
                    cor = COLOR_EXIT
                elif cell in bloqueados:
                    cor = COLOR_BLOCK
                self.itemconfig(self.celulas[i][j], fill=cor)

# Thread da animação
class Animation(Thread):
    def __init__(self, algoritmo):
        super().__init__()
        self.algoritmo = algoritmo

    def run(self):
        gifWindow = tk.Toplevel()
        gifWindow.title("Aguarde")
        gifWindow.resizable(0, 0)
        gifWindow.geometry("628x542")

        try:
            icon = tk.PhotoImage(file='favicon.png')
            gifWindow.iconphoto(False, icon)
        except Exception as e:
            print('Ícone não encontrado!', e)

        texto = tk.Label(gifWindow, text="Gerando animação, aguarde...")
        texto.pack(pady=20)

        gif_path = ""
        if self.algoritmo == 'breadthFirstSearch':
            breadthFirstSearch(gato[0], saida[0], bloqueados)
            gif_path = "Gifs/Gif_Amplitude.gif"
        elif self.algoritmo == 'depthFirst':
            depthFirst(gato[0], saida[0], bloqueados)
            gif_path = "Gifs/Gif_Profundidade.gif"
        elif self.algoritmo == 'bestFirst':
            bestFirst(gato[0], saida[0], bloqueados)
            gif_path = "Gifs/Gif_Melhor-Primeiro.gif"
        elif self.algoritmo == 'aStar':
            aStar(gato[0], saida[0], bloqueados)
            gif_path = "Gifs/Gif_aStar.gif"

        texto.destroy()
        gif = Gif(gifWindow, gif_path)
        gif.pack()
        gif.run(interval=delayGif, n_repeats=-1)

# Funções de seleção
def select(cell):
    global SELECTED
    if SELECTED == 'GATO':
        if cell in bloqueados:
            bloqueados.remove(cell)
        if saida and saida[0] == cell:
            saida.clear()
        if not gato:
            gato.append(cell)
        else:
            gato[0] = cell
        tabuleiro.atualizar_cores()

    elif SELECTED == 'SAIDA':
        if cell in bloqueados:
            bloqueados.remove(cell)
        if gato and gato[0] == cell:
            gato.clear()
        if not saida:
            saida.append(cell)
        else:
            saida[0] = cell
        tabuleiro.atualizar_cores()

    elif SELECTED == 'BLOQUEIOS':
        if gato and cell == gato[0]:
            gato.clear()
        if saida and cell == saida[0]:
            saida.clear()
        if cell not in bloqueados:
            bloqueados.append(cell)
        else:
            bloqueados.remove(cell)
        tabuleiro.atualizar_cores()

# Função para selecionar tipo de elemento
def set_selection(tipo):
    global SELECTED
    SELECTED = tipo
    for key, btn in selection_buttons.items():
        btn.configure(bg=COLOR_SELECTED if key == tipo else COLOR_UNSELECTED)

# Inicializa janela
root = tk.Tk()
root.title("Visualização de Buscas Cegas e Heurísticas - By Alfredo Albélis; Pedro Bernini. (2020)")
root.geometry("1000x700")
root.configure(bg=BACKGROUND_COLOR)
try:
    root.tk.call('wm', 'iconphoto', root._w, tk.Image('photo', file='favicon.png'))
except:
    print('Ícone não encontrado!')

# Frame de seleção
selection_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
selection_frame.pack(pady=10)

selection_buttons = {}
for label in ['GATO', 'BLOQUEIOS', 'SAIDA']:
    btn = tk.Button(selection_frame, text=label, width=20, fg=TXT_BTN_COLOR,
                    bg=COLOR_SELECTED if label == 'GATO' else COLOR_UNSELECTED,
                    command=lambda l=label: set_selection(l))
    btn.pack(side='left', padx=5)
    selection_buttons[label] = btn

btn_clear = tk.Button(selection_frame, text="LIMPAR", bg='red', fg=TXT_BTN_COLOR,
                      command=lambda: [gato.clear(), saida.clear(), bloqueados.clear(), tabuleiro.atualizar_cores()])
btn_clear.pack(side='left', padx=5)

# Tabuleiro com Canvas
board_frame = tk.Frame(root, bg=TABULEIRO_BG_COLOR)
board_frame.pack(fill='both', expand=True, padx=20, pady=10)

tabuleiro = TabuleiroCanvas(board_frame, linhas=11, colunas=11, bg='gray', highlightthickness=0)
tabuleiro.pack(fill='both', expand=True)

# Algoritmos
algo_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
algo_frame.pack(pady=20)

def iniciar_busca(nome):
    if not gato or not saida:
        messagebox.showinfo("Erro", "Selecione ponto inicial e final.")
        return
    Animation(nome).start()

for nome, label in [('aStar', 'A*'), ('bestFirst', 'Melhor-Primeiro'),
                    ('breadthFirstSearch', 'Amplitude'), ('depthFirst', 'Profundidade')]:
    tk.Button(algo_frame, text=label, width=20, bg='#43b581', fg='white',
              command=lambda n=nome: iniciar_busca(n)).pack(side='left', padx=5)

# Velocidade
speed_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
speed_frame.pack(pady=10)

def set_speed(nome):
    global delayGif
    delayGif = DELAY_MAP[nome]
    for k, b in speed_buttons.items():
        b.configure(bg=COLOR_SELECTED if k == nome else COLOR_UNSELECTED)

speed_buttons = {}
for label in DELAY_MAP:
    b = tk.Button(speed_frame, text=label, width=12, fg='white',
                  bg=COLOR_SELECTED if label == 'Normal' else COLOR_UNSELECTED,
                  command=lambda l=label: set_speed(l))
    b.pack(side='left', padx=2)
    speed_buttons[label] = b

# Legenda
legend_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
legend_frame.pack(pady=5)

tk.Label(legend_frame, text="Legenda:", bg=BACKGROUND_COLOR, fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=(0, 10))
tk.Label(legend_frame, text="Gato", bg=COLOR_CAT, fg='white', width=8).pack(side='left', padx=2)
tk.Label(legend_frame, text="Nó Aberto", bg=COLOR_OPEN_NODE, fg='white', width=10).pack(side='left', padx=2)
tk.Label(legend_frame, text="Nó Fechado", bg=COLOR_CLOSED_NODE, fg='white', width=10).pack(side='left', padx=2)
tk.Label(legend_frame, text="Bloqueio", bg=COLOR_BLOCK, fg='white', width=10).pack(side='left', padx=2)
tk.Label(legend_frame, text="Saída", bg=COLOR_EXIT, fg='white', width=8).pack(side='left', padx=2)
tk.Label(legend_frame, text="Vazio", bg='white', fg='black', width=8).pack(side='left', padx=2)

# Créditos
credits_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
credits_frame.pack(pady=2)

def abrir_github_alfredo(event):
    webbrowser.open_new("https://github.com/AlfredoFilho/")

def abrir_github_pedro(event):
    webbrowser.open_new("https://github.com/PedroBernini")

tk.Label(credits_frame, text="Desenvolvido por", bg=BACKGROUND_COLOR, fg='white', font=('Arial', 8)).pack(side='left')

# Alfredo
alfredo_label = tk.Label(credits_frame, text="Alfredo Albélis", bg=BACKGROUND_COLOR, fg='skyblue', cursor='hand2', font=('Arial', 8, 'underline'))
alfredo_label.pack(side='left', padx=(5, 0))
alfredo_label.bind("<Button-1>", abrir_github_alfredo)

tk.Label(credits_frame, text="e", bg=BACKGROUND_COLOR, fg='white', font=('Arial', 8)).pack(side='left')

# Pedro
pedro_label = tk.Label(credits_frame, text="Pedro Bernini", bg=BACKGROUND_COLOR, fg='skyblue', cursor='hand2', font=('Arial', 8, 'underline'))
pedro_label.pack(side='left')
pedro_label.bind("<Button-1>", abrir_github_pedro)

# Caminho do log (exemplo fictício)
log_path_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
log_path_frame.pack(pady=2)

tk.Label(log_path_frame, text="Logs completos dos algoritmos salvos em: /Logs/Log_<Algoritmo>.txt", bg=BACKGROUND_COLOR, fg='white', font=('Arial', 8)).pack()

root.mainloop()
