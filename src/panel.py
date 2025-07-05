import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Panel Example")

        self.panel1 = tk.Frame(self, bg="lightblue")
        tk.Label(self.panel1, text="Panel 1 Content").pack(pady=20)
        self.panel1.pack(fill="both", expand=True)

        self.panel2 = tk.Frame(self, bg="lightgreen")
        tk.Label(self.panel2, text="Panel 2 Content").pack(pady=20)

        self.switch_button = tk.Button(self, text="Switch Panel", command=self.switch_panels)
        self.switch_button.pack(pady=10)

        self.current_panel = self.panel1

    def switch_panels(self):
        if self.current_panel == self.panel1:
            self.panel1.pack_forget()
            self.panel2.pack(fill="both", expand=True)
            self.current_panel = self.panel2
        else:
            self.panel2.pack_forget()
            self.panel1.pack(fill="both", expand=True)
            self.current_panel = self.panel1

if __name__ == "__main__":
    app = App()
    app.mainloop()