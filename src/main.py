import tkinter as tk
from tkinter import ttk, messagebox
from DispLabel import  DispLabel
from LabelUI import MSLabel  # Assuming LabelUI is defined in LabelUI.py
from LabelUI import LabelUI  # Assuming LabelUI is defined in LabelUI.py
from HalbLabel import HalbLabel
from CleaningLabel import CleaningLabel
from MSLabel import MSLabel  # Assuming MSLabel is defined in MSLabel.py

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barcode/QR Code Generator")
        self.root.geometry("900x750")
        notebook = ttk.Notebook(root)
        notebook.pack(expand=True, fill="both")
        tab_msl = LabelUI(notebook, MSLabel, file_path="output/ms_labels.csv")  # Assuming LabelUI takes a model class and a file path
        notebook.add(tab_msl, text="Material Status Label")
        tab_disp = LabelUI(notebook, DispLabel, file_path="output/disp_labels.csv")
        notebook.add(tab_disp, text="Dispensing Label")
        tab_cleaning = LabelUI(notebook, CleaningLabel, file_path="output/cleaning_labels.csv")
        notebook.add(tab_cleaning, text="Cleaning Label")
        tab_halb = LabelUI(notebook, HalbLabel, file_path="output/halb_labels.csv")
        notebook.add(tab_halb, text="Halb Label")



if __name__ == "__main__":
    MainApp(tk.Tk()).root.mainloop()
