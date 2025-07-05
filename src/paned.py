import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("PanedWindow Example")

# Create a PanedWindow
paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill="both", expand=True)

# Create two frames to act as panes
frame1 = ttk.Frame(paned_window, width=200, height=150, relief="sunken")
frame2 = ttk.Frame(paned_window, width=400, height=150, relief="sunken")

# Add some content to the frames
tk.Label(frame1, text="Pane 1").pack(padx=10, pady=10)
tk.Label(frame2, text="Pane 2").pack(padx=10, pady=10)

# Add the frames to the PanedWindow
paned_window.add(frame1)
paned_window.add(frame2)

root.mainloop()