import tkinter as tk
from tkinter import ttk, filedialog
import csv


class CSVViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Table Viewer")
        self.root.geometry("800x600")

        # Table (Treeview)
        self.tree = ttk.Treeview(root, show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        vsb = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        vsb.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=vsb.set)

        hsb = ttk.Scrollbar(root, orient="horizontal", command=self.tree.xview)
        hsb.pack(side='bottom', fill='x')
        self.tree.configure(xscrollcommand=hsb.set)

        # Menu
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open CSV", command=self.load_csv)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

    def load_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not filepath:
            return

        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        if not rows:
            return

        headers = rows[0]
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = headers

        # Set columns
        for col in headers:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='w')

        # Insert data
        for row in rows[1:]:
            self.tree.insert("", "end", values=row)


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewerApp(root)
    root.mainloop()