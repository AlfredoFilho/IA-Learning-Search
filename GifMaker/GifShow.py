# -*- coding: utf-8 -*-
import tkinter as tk

class Gif (tk.Label):

	def __init__(self, root, gif):
		tk.Label.__init__(self, root)
		self._img  = tk.PhotoImage(file=gif)
		self.image = self._img
		self.configure(image=self._img)

	def run(self, interval=150, n_repeats=-1):
		self.n_repeats = n_repeats
		self._play_gif(interval)
		
	def _play_gif(self, interval):
		self.configure(image=self._img) 
		self.frame = 0
		self.repeats = 0
		self._next_frame(interval)
            
	def _next_frame(self, interval):
		try:
			opt = "GIF -index {}".format(self.frame)
			self._img.configure(format=opt)
		except tk.TclError:
			self.frame = 0
			self.repeats += 1
			if (self.repeats >= self.n_repeats and self.n_repeats > 0):
				opt = "GIF -index {}".format(0)
				self._img.configure(format=opt)
				return
			else:
				self._next_frame(interval)
				return
		self.frame += 1
		self.after(interval, self._next_frame, interval)
