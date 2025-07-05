import tkinter as tk
from MSLabel import MSLabelUI  # Assuming MSLabelUI is defined in MSLabel.py
from tkinter import ttk, messagebox
from MSLabel import MSLabelUI
from DispLabel import DispLabelUI

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barcode/QR Code Generator")
        self.root.geometry("1000x1000")
        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill="both")
        tab_msl = MSLabelUI(notebook)
        tab_disp = DispLabelUI(notebook)
        notebook.add(tab_msl, text="MS Label")
        notebook.add(tab_disp, text="Disp Label")   

if __name__ == "__main__":
    MainApp(tk.Tk()).root.mainloop()
