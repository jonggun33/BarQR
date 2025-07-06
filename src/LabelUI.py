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
        self.laod_csv()

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
        self.contents = ttk.Label(frm, text = "")
        self.contents.grid(row=row, column=2, sticky='ew', pady=10)
        show_btn = ttk.Button(frm, text="Show Bar/QR code", command=self.show_barcode)
        show_btn.grid(row=row, column=0, columnspan=2, pady=10)
        save_btn = ttk.Button(frm, text="Save", command=self.save)
        save_btn.grid(row=row, column=1, columnspan=2, pady=10)
        frm.columnconfigure(1, weight=1)

        sep = ttk.Separator(frm, orient='horizontal')
        # Make the treeview expand to fill available vertical space
        frm.rowconfigure(row+2, weight=1)
        sep.grid(row=row+1, column=0, columnspan=3, sticky='ew', pady=10 )
        self.tree = ttk.Treeview(frm, show='headings', height=20)
        self.tree.grid(row=row+2, column=0, columnspan=3, sticky='nsew')
        vsb = ttk.Scrollbar(frm, orient="vertical", command=self.tree.yview)
        vsb.grid(row=row+2, column=3, sticky='ns')
        hsb = ttk.Scrollbar(frm, orient="horizontal", command=self.tree.xview)
        hsb.grid(row=row+3, column=0, columnspan=3, sticky='ew')
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.bind("<<TreeviewSelect>>", self._on_row_select)

    def _on_row_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        columns = self.tree["columns"]
        for idx, field in enumerate(columns):
            if field in self.inputs:
                self.inputs[field].delete(0, tk.END)
                self.inputs[field].insert(0, values[idx])

    def save(self):
        self._fill_model()
        data = self.model.__dict__
        file_exists = os.path.isfile(self.file_path)
        # Check for duplicate row
        duplicate = False
        if file_exists:
            with open(self.file_path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if all(str(row.get(k, "")) == str(data.get(k, "")) for k in data.keys()):
                        duplicate = True
                        break
        if duplicate:
            messagebox.showwarning("Duplicate", "This label already exists!")
            return
        with open(self.file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
        messagebox.showinfo("Success", "Label saved successfully!")
        self.laod_csv()
    def show_barcode(self):
        self._fill_model()
        if self.model_cls.__name__ == 'MSLabel':
            generated_img = qrcode.make(self.model.__str__())
            generated_img = generated_img.resize((300, 300))  # Resize for better display
            self.contents.config(text=str(self.model))
        elif self.model_cls.__name__ == 'DispLabel':
            barcode_class = barcode.get_barcode_class("code128")
            code = barcode_class(str(self.model), writer=barcode.writer.ImageWriter())
            buffer = io.BytesIO()
            code.write(buffer)
            buffer.seek(0)
            generated_img = Image.open(buffer)
            generated_img = generated_img.resize((480, 180))  # Resize for better display
            self.contents.config(text=str(self.model))
        elif self.model_cls.__name__ == 'HalbLabel':
            barcode_class = barcode.get_barcode_class("code128")
            code = barcode_class(str(self.model), writer=barcode.writer.ImageWriter())
            buffer = io.BytesIO()
            code.write(buffer)
            buffer.seek(0)
            generated_img = Image.open(buffer)
            generated_img = generated_img.resize((480, 180))  # Resize for better display
            self.contents.config(text=str(self.model))
        elif self.model_cls.__name__ == 'CleaningLabel':
            barcode_class = barcode.get_barcode_class("code128")
            code = barcode_class(str(self.model), writer=barcode.writer.ImageWriter())
            buffer = io.BytesIO()
            code.write(buffer)
            buffer.seek(0)
            generated_img = Image.open(buffer)
            generated_img = generated_img.resize((480, 180))  # Resize for better display
            self.contents.config(text=str(self.model))
        # Resize image to fit inside the canvas while maintaining aspect ratio
        img_w, img_h = generated_img.size
        canvas_w = int(self.canvas['width'])
        canvas_h = int(self.canvas['height'])
        scale = min(canvas_w / img_w, canvas_h / img_h, 1.0)
        new_w = int(img_w * scale)
        new_h = int(img_h * scale)
        resized_img = generated_img.resize((new_w, new_h), Image.LANCZOS)
        tk_img = ImageTk.PhotoImage(resized_img)
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
    def laod_csv(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.tree.delete(*self.tree.get_children())
            self.tree["columns"] = list(reader.fieldnames)
            for col in self.tree["columns"]:
                self.tree.heading(col, text=col)
                self.tree.column(col, anchor='w')
            for row in reader:
                self.tree.insert("", "end", values=list(row.values()))

# Example model class

@dataclass
class LabelModel:
    name: str
    code: str
    price: str

if __name__ == "__main__":
    app = LabelUI(MSLabel)
    app.mainloop()