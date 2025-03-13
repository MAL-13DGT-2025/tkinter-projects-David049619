import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("D's Lemonade")


selected_lemonade = tk.StringVar(value="")
selected_size = tk.StringVar(value="")
selected_ice = tk.StringVar(value="No Ice")
selected_sugar = tk.StringVar(value="No Sugar")
total_price = tk.IntVar(value=0)

# 1. Title
title = ttk.Label(root, text="D's Lemonade", font=("Arial", 16, "bold")).grid(row=0, column=1, pady=10)

# 2. Lemonade Type Selection
chooice = ttk.Label(root, text="Choose Your Lemonade:", font=("Arial", 12, "bold")).grid(row=1, column=1, pady=5)
pink = ttk.Button(root, text="Pink Lemonade", command=lambda: selected_lemonade.set("Pink Lemonade")).grid(row=2, column=0)
cloudy = ttk.Button(root, text="Cloudy Lemonade", command=lambda: selected_lemonade.set("Cloudy Lemonade")).grid(row=2, column=1)
brown = ttk.Button(root, text="Brown Lemonade", command=lambda: selected_lemonade.set("Brown Lemonade")).grid(row=2, column=2)

# 3. Size Selection
choice1 = ttk.Label(root, text="Choose Size:", font=("Arial", 12, "bold")).grid(row=3, column=1, pady=5)
small = ttk.Button(root, text="Small $6", command=lambda: [selected_size.set("Small")]).grid(row=4, column=0)
medium = ttk.Button(root, text="Medium $8", command=lambda: [selected_size.set("Medium")]).grid(row=4, column=1)
large = ttk.Button(root, text="Large $10", command=lambda: [selected_size.set("Large")]).grid(row=4, column=2)

option = ttk.Label(root, text="Ice Option:", font=("Arial", 12, "bold")).grid(row=5, column=1, pady=5)
ice = ttk.Button(root, text="No Ice", command=lambda: selected_ice.set("No Ice")).grid(row=6, column=0, columnspan=3)
ice1 = ttk.Button(root, text="Ice", command=lambda: selected_ice.set("Ice")).grid(row=6, column=1)

# 5. Sugar Option (Centered)
option2 = ttk.Label(root, text="Sugar Option:", font=("Arial", 12, "bold")).grid(row=7, column=1, pady=5)
sugar = ttk.Button(root, text="No Sugar", command=lambda: selected_sugar.set("No Sugar")).grid(row=8, column=0, columnspan=3)
sugar1 = ttk.Button(root, text="Sugar", command=lambda: selected_sugar.set("Sugar")).grid(row=8, column=1)



# Run the application
root.mainloop()
