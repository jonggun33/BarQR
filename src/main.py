import tkinter as tk
from tkinter import ttk, messagebox
from DispLabel import  DispLabel
from LabelUI import MSLabel  # Assuming LabelUI is defined in LabelUI.py
from LabelUI import LabelUI  # Assuming LabelUI is defined in LabelUI.py

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barcode/QR Code Generator")
        self.root.geometry("1000x1000")
        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill="both")
        #tab_msl = MSLabelUI(notebook)
        #tab_disp = DispLabelUI(notebook)
        #notebook.add(tab_msl, text="MS Label")
        #notebook.add(tab_disp, text="Disp Label")   
        tab_msl = LabelUI(notebook, MSLabel, file_path="output/ms_labels.csv")  # Assuming LabelUI takes a model class and a file path
        notebook.add(tab_msl, text="Label UI")
        tab_disp = LabelUI(notebook, DispLabel, file_path="output/disp_labels.csv")
        notebook.add(tab_disp, text="Disp Label UI")


if __name__ == "__main__":
    MainApp(tk.Tk()).root.mainloop()
