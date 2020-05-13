import tkinter as tk

def resultado(s):
	root = tk.Tk()

	w = tk.Label(root, text=s)
	w.configure(anchor="center")
	w.pack()

	root.mainloop()