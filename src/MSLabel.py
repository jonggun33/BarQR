from pydantic import BaseModel, Field
import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk

class MSLabel(BaseModel):
    mat_code: str = Field(..., description="Material code for the label")
    control_no: str = Field(..., description="Control number for the label")

class MSLabelUI(ttk.Frame):
    """UI for generating MS labels with material code and control number, displayed neatly in a tab view frame."""
    def __init__(self, parent):
        super().__init__(parent)

        # Main frame for padding and layout
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        ttk.Label(main_frame, text="MS Label Generator", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Material code input
        ttk.Label(main_frame, text="Material Code:").grid(row=1, column=0, sticky=tk.E, pady=5, padx=(0, 10))
        self.mat_code_entry = ttk.Entry(main_frame, width=40)
        self.mat_code_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Control number input
        ttk.Label(main_frame, text="Control Number:").grid(row=2, column=0, sticky=tk.E, pady=5, padx=(0, 10))
        self.control_no_entry = ttk.Entry(main_frame, width=40)
        self.control_no_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Generate button
        self.generate_btn = ttk.Button(main_frame, text="Generate", command=self.generate_label)
        self.generate_btn.grid(row=3, column=0, columnspan=2, pady=15)

        # Image display area
        self.canvas = tk.Canvas(main_frame, width=200, height=200, bg='white', highlightthickness=1, highlightbackground="#ccc")
        self.canvas.grid(row=4, column=0, columnspan=2, pady=10)

        # Configure grid weights for resizing
        main_frame.columnconfigure(0, weight=0)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)

    def generate_label(self):
        mat_code = self.mat_code_entry.get().strip()
        control_no = self.control_no_entry.get().strip()
        label = MSLabel(
            mat_code=mat_code,
            control_no=control_no
        )
        generated_img = qrcode.make(label.json())
        tk_img = ImageTk.PhotoImage(generated_img.resize((180, 180)))
        self.canvas.delete("all")
        self.canvas.create_image(100, 100, image=tk_img)
        self.canvas.image = tk_img  # Keep a reference to avoid garbage collection  


