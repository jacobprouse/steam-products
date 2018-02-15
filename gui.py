import function
import tkinter as tk
from tkinter import Tk, StringVar, ttk, END
from tkinter.ttk import *

class SteamApp(tk.Frame):
	def __init__(self, master):
		super(SteamApp, self).__init__()
		self.master = master
		master.title("Steam Content")
		self.grid(column=0,row=0)
		self.create_widgets()


	def create_widgets(self):
		
		#combo box for selection
		self.combo_value = StringVar()
		self.search_combo = ttk.Combobox(self, textvariable = self.combo_value)
		self.search_combo['values'] = ("Top Sellers", "Specials", "Upcoming")
		self.search_combo.current(0)
		self.search_combo.pack(side = "top")

		#search button
		self.searchButton = ttk.Button(self, text = "Search", command = self.steam_content)
		self.searchButton["text"] = "Search"
		self.searchButton.pack(side = "bottom")


		#text area
		self.textArea = tk.Text(self, height = 30, width = 50)
		self.textArea.pack(side = "right")

		#quit button
		self.quitButton = ttk.Button(self, text = "Quit", command = root.destroy)
		self.quitButton.pack(side = "bottom")

	def steam_content(self):
			name_array = []
			name_array = function.steamContent(self.combo_value.get())

			for elements in name_array:
				self.textArea.insert(END, elements + "\n")
	


if __name__ == '__main__':
	root = Tk()
	app = SteamApp(root)
	root.mainloop()
