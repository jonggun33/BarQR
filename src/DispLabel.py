from pydantic import BaseModel, Field
import barcode
from tkinter import ttk
import tkinter as tk
from PIL import Image
import io
from PIL import ImageTk

class DispLabel(BaseModel):
    """
    Model for displaying a label with a code type, material code, and control number.
    This model is used to represent the data structure for a label in the application.
    """
    proc_order: str = Field(..., description="Process order for the label")
    mat_code: str = Field(..., description="Material code for the label")
    container_id: str = Field(..., description="Container ID for the label")
    def __str__(self):
        """
        Returns a string representation of the DispLabel instance.
        This is useful for debugging and logging purposes.
        """
        return f"{self.proc_order}_{self.mat_code}_{self.container_id}"
    
class DispLabelUI(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        """
        Initializes the DispLabelUI as a Frame.
        This UI is designed to be embedded within a tab or another container.
        """
        super().__init__(parent, *args, **kwargs)

        # Main frame for padding and neat layout
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(main_frame, text="Process Order:").pack(pady=5)
        self.proc_order_entry = ttk.Entry(main_frame, width=50)
        self.proc_order_entry.pack(pady=5)  
        ttk.Label(main_frame, text="Material Code:").pack(pady=5)
        self.mat_code_entry = ttk.Entry(main_frame, width=50)
        self.mat_code_entry.pack(pady=5)
        ttk.Label(main_frame, text="Container ID:").pack(pady=5)
        self.container_id_entry = ttk.Entry(main_frame, width=50)
        self.container_id_entry.pack(pady=5)    

        self.generate_btn = ttk.Button(main_frame, text="Generate", command=self.generate_label)
        self.generate_btn.pack(pady=10) 
        self.label_display = ttk.Label(main_frame, text="", font=("Arial", 14))
        self.label_display.pack(pady=10)    
        self.canvas = tk.Canvas(main_frame, width=500, height=300, bg='white')
        self.canvas.pack(pady=10)

    def generate_label(self):
        proc_order = self.proc_order_entry.get().strip()
        mat_code = self.mat_code_entry.get().strip()
        container_id = self.container_id_entry.get().strip()
        label = DispLabel(
            proc_order=proc_order,
            mat_code=mat_code,
            container_id=container_id
        )
        barcode_class = barcode.get_barcode_class("code128")
        code = barcode_class(str(label), writer=barcode.writer.ImageWriter())
        buffer = io.BytesIO()
        code.write(buffer)
        buffer.seek(0)
        generated_img = Image.open(buffer)
        tk_img = ImageTk.PhotoImage(generated_img)
        self.canvas.create_image(150, 150, image=tk_img)
        self.canvas.image = tk_img  # Keep a reference to avoid garbage collection
