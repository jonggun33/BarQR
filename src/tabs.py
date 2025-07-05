import tkinter as tk
from tkinter import ttk
from MSLabel import MSLabelUI  # Assuming MSLabelUI is defined in MSLabel.py
class MyFrame(ttk.Frame):
    """Custom frame for MSLabelUI."""
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = MSLabelUI(self)  # Initialize MSLabelUI within this frame
        self.ui.pack(expand=True, fill="both")  # Pack the UI to fill the frame
root = tk.Tk()
root.title("Tabbed Interface Example")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Create frames for each tab
tab1_frame = ttk.Frame(notebook)
tab2_frame = ttk.Frame(notebook)
tab3_frame = MSLabelUI(notebook)

# Add frames as tabs
notebook.add(tab1_frame, text="Tab 1")
notebook.add(tab2_frame, text="Tab 2")
notebook.add(tab3_frame, text="My Frame")


root.mainloop()