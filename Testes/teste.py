from tkinter import *
import tkinter as tk

def changeButton() :
    global button
    button["cursor"] = "hand2"
    button["bg"] = "green"

class CustomButton(tk.Canvas):
    def __init__(self, parent, width, height, color, command=None, cur=None):
        tk.Canvas.__init__(self, parent, borderwidth=1, 
            relief="raised", highlightthickness=0)
        self.command = command

        padding = 4
        id = self.create_oval((padding,padding,
            width+padding, height+padding), outline=color, fill=color)
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0) + padding
        height = (y1-y0) + padding
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        
    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

app = tk.Tk()
button = CustomButton(app, 25, 25, 'red', command=changeButton, cur="hand2")
button.pack()
app.mainloop()