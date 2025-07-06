import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from dataclasses import dataclass
from MSLabel import MSLabel  # Assuming MSLabel is defined in MSLabel.py
import os
import csv
import qrcode
import barcode
import io

class LabelUI(ttk.Frame):
    def __init__(self, parent, model_cls, file_path):
        super().__init__(parent)
        self.model_cls = model_cls
        self.model = None
        self.inputs = {}
        self._build_ui()
        self.file_path  = file_path

    def _build_ui(self):
        frm = ttk.Frame(self)
        frm.pack(padx=10, pady=10, fill='x')
        row = 0
        for field in self.model_cls.__annotations__:
            ttk.Label(frm, text=field).grid(row=row, column=0, sticky='w', pady=2)
            entry = ttk.Entry(frm)
            entry.grid(row=row, column=1, sticky='ew', pady=2, ipadx=30)
            self.inputs[field] = entry
            row += 1
        # Canvas for image/label preview
        self.canvas = tk.Canvas(frm, width=300, height=300, bg='white')
        self.canvas.grid(row=0, column=2, rowspan=row, padx=10)
        show_btn = ttk.Button(frm, text="Show Bar/QR code", command=self.show_barcode)
        show_btn.grid(row=row, column=0, columnspan=2, pady=10)
        save_btn = ttk.Button(frm, text="Save", command=self.save)
        save_btn.grid(row=row, column=1, columnspan=2, pady=10)
        frm.columnconfigure(1, weight=1)

    def save(self):
        self._fill_model()
        data = self.model.__dict__
        file_exists = os.path.isfile(self.file_path)
        with open(self.file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
        messagebox.showinfo("Success", "Label saved successfully!")
    def show_barcode(self):
        self._fill_model()
        if self.model_cls.__name__ == 'MSLabel':
            generated_img = qrcode.make(self.model.json())
            generated_img = generated_img.resize((300, 300))  # Resize for better display
        elif self.model_cls.__name__ == 'DispLabel':
            barcode_class = barcode.get_barcode_class("code128")
            code = barcode_class(str(self.model), writer=barcode.writer.ImageWriter())
            buffer = io.BytesIO()
            code.write(buffer)
            buffer.seek(0)
            generated_img = Image.open(buffer)
            generated_img = generated_img.resize((480, 180))  # Resize for better display
        tk_img = ImageTk.PhotoImage(generated_img)
        self.canvas.delete("all")
        # Center the image in the canvas
        canvas_width = int(self.canvas['width'])
        canvas_height = int(self.canvas['height'])
        x = canvas_width // 2
        y = canvas_height // 2
        self.canvas.create_image(x, y, image=tk_img)
        self.canvas.image = tk_img  # Keep a reference to avoid garbage collection

    def _fill_model(self):
        data = {}
        for field, entry in self.inputs.items():
            data[field] = entry.get()
        try:
            self.model = self.model_cls(**data)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Example model class

@dataclass
class LabelModel:
    name: str
    code: str
    price: str

if __name__ == "__main__":
    app = LabelUI(MSLabel)
    app.mainloop()