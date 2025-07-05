import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import qrcode
import barcode
from barcode.writer import ImageWriter
import io

class CodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barcode/QR Code Generator")
        self.root.geometry("500x550")

        # Content input
        ttk.Label(root, text="Enter Content:").pack(pady=5)
        self.content_entry = ttk.Entry(root, width=50)
        self.content_entry.pack(pady=5)

        # Code type selector
        ttk.Label(root, text="Select Code Type:").pack(pady=5)
        self.code_type = ttk.Combobox(root, values=["QR Code", "EAN13", "Code128"], state="readonly")
        self.code_type.current(0)
        self.code_type.pack(pady=5)

        # Generate button
        self.generate_btn = ttk.Button(root, text="Generate", command=self.generate_code)
        self.generate_btn.pack(pady=10)

        # Image display area
        self.canvas = tk.Canvas(root, width=300, height=300, bg='white')
        self.canvas.pack(pady=10)

        # Save button
        self.save_btn = ttk.Button(root, text="Save Image", command=self.save_image)
        self.save_btn.pack(pady=5)

        # Image storage
        self.generated_img = None
        self.tk_img = None

    def generate_code(self):
        content = self.content_entry.get().strip()
        code_type = self.code_type.get()

        if not content:
            messagebox.showerror("Error", "Please enter content.")
            return

        try:
            # Enforce string type
            content = str(content)
            print(f"[DEBUG] Code Type: {code_type}, Content: {content}, Type: {type(content)}")

            if code_type == "QR Code":
                qr = qrcode.make(content)
                print(qr)
                self.generated_img = qr

            elif code_type == "EAN13":
                if not content.isdigit():
                    raise ValueError("EAN13 requires numeric input.")
                if len(content) != 12:
                    raise ValueError("EAN13 requires exactly 12 digits.")

                barcode_class = barcode.get_barcode_class("ean13")
                code = barcode_class(str(content), writer=ImageWriter())
                buffer = io.BytesIO()
                code.write(buffer)
                buffer.seek(0)
                self.generated_img = Image.open(buffer)

            elif code_type == "Code128":
                barcode_class = barcode.get_barcode_class("code128")
                code = barcode_class(str(content), writer=ImageWriter())
                buffer = io.BytesIO()
                code.write(buffer)
                buffer.seek(0)
                self.generated_img = Image.open(buffer)

            else:
                raise ValueError("Unsupported code type.")

            self.show_image(self.generated_img)

        except Exception as e:
            print(f"[ERROR] {type(e).__name__}: {e}")
            messagebox.showerror("Generation Error", f"{type(e).__name__}: {e}")

    def show_image(self, pil_img):
        try:
            img = pil_img.copy().convert("RGB")  # ensure compatible mode
            # Resize image to fit the canvas
            #img.thumbnail((300, 300))
            print(f"[DEBUG] img mode: {img.mode}, size: {img.size}, type: {type(img)}")
            self.tk_img = ImageTk.PhotoImage(img)
            print(f"[DEBUG] Image size: {img.size}, Mode: {img.mode}")
            self.canvas.delete("all")
            self.canvas.create_image(150, 150, image=self.tk_img)
        except Exception as e:
            print(f"[ERROR in show_image] {type(e).__name__}: {e}")
            messagebox.showerror("Image Display Error", f"{type(e).__name__}: {e}")

    def save_image(self):
        if self.generated_img is None:
            messagebox.showerror("Error", "No image to save.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")]
        )
        if file_path:
            try:
                self.generated_img.save(file_path)
                messagebox.showinfo("Saved", f"Image saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Save Error", f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeGeneratorApp(root)
    root.mainloop()