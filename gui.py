import function
import tkinter as tk
from tkinter import Tk, StringVar, ttk
from tkinter.ttk import *
#from tkinter.tkk import *

class SteamApp:
	def __init__(self, master):
		self.master = master
		master.title("Steam Content")
		self.create_widgets()

	def create_widgets(self):
		
		#combo box for selection
		self.combo_value = StringVar()
		self.search_combo = ttk.Combobox(self.master, textvariable = self.combo_value)
		self.search_combo['values'] = ("Top Sellers", "Specials", "Upcoming")
		self.search_combo.current(0)
		self.search_combo.grid(column = 0, row = 0)

		def search_steam(value):
			printSteamContent(value)

		#search button
		self.searchButton = ttk.Button(self, text = "Search", command = search_steam())
		self.searchButton["text"] = "Search"
		self.searchButton["command"] = self.search_steam
		self.searchButton.pack(side = "bottom")

		#quit button
		self.quitButton = ttk.Button(self, text = "Quit", fg = "red",
									command = root.destroy)
		self.quit.pack(side = "bottom")

if __name__ == '__main__':
	root = Tk()
	app = SteamApp(root)
	root.mainloop()
