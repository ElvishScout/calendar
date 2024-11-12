import tkinter as tk
from utils import set_dpi_aware, move_window_desktop, restore_window

set_dpi_aware()

# Initialize the main window
root = tk.Tk()
root.title("Desktop Calendar")
root.geometry("400x400")
root.attributes("-toolwindow", True)

# Stick to desktop button
stick_button = tk.Button(root, text="Stick to Desktop", command=lambda: move_window_desktop(root))
stick_button.pack(pady=10)

# Restore window button
restore_button = tk.Button(root, text="Restore Window", command=lambda: restore_window(root))
restore_button.pack(pady=10)

root.mainloop()
