import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        visualize_data(df)

def visualize_data(data):
    plt.clf()  # Clear the previous plot
    plt.bar(data['Category'], data['Value'])
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.title('CSV Data Visualization')
    plt.xticks(rotation=45)
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("CSV Data Visualization")

# Create a button to open CSV file
open_button = tk.Button(root, text="Open CSV File", command=open_file)
open_button.pack()

# Create a Matplotlib figure for the plot
fig = plt.figure(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Start the Tkinter event loop
root.mainloop()
