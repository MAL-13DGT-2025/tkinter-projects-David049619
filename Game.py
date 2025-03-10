import tkinter as tk 
from tkinter import ttk



root = tk.Tk() # MUST HAVE

root.title("Game")


title = ttk.Label(root, text = "Rock\nPaper\nScissor")
title.grid(row = 0, column = 0, columnspan = 3, padx = 50, pady = 10)

b_1 = ttk.Button(root, text = "Rock", command = lambda:press("Rock"))
b_1.grid(row = 2, column = 0)

b_2 = ttk.Button(root, text = "Paper", command = lambda:press("Paper"))
b_2.grid(row = 2, column = 1)
         
b_3 = ttk.Button(root, text = "scissors", command = lambda:press("Scissors"))
b_3.grid(row = 2, column = 2)

title = ttk.Label(root, text = "")
title.grid(row = 3, column = 0, columnspan = 3, padx = 50, pady = 10)


root.mainloop()