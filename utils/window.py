import tkinter as tk
import ctypes

HWND_BOTTOM = 1
SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002
SWP_NOACTIVATE = 0x0010
GWL_STYLE = -16
WS_CHILD = 0x40000000
WS_VISIBLE = 0x10000000


SetParent = ctypes.windll.user32.SetParent
SetWindowLong = ctypes.windll.user32.SetWindowLongW
GetDesktopWindow = ctypes.windll.user32.GetDesktopWindow
SetProcessDpiAwareness = ctypes.windll.shcore.SetProcessDpiAwareness
SetWindowPos = ctypes.windll.user32.SetWindowPos


def set_dpi_aware():
    SetProcessDpiAwareness(True)


def move_window_bottom(root: tk.Tk):
    hwnd = int(root.frame(), 16)

    SetWindowPos(hwnd, HWND_BOTTOM, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE | SWP_NOACTIVATE)


def move_window_desktop(root: tk.Tk):
    root.overrideredirect(True)

    hwnd = int(root.frame(), 16)
    desktop_hwnd = GetDesktopWindow()

    SetParent(hwnd, desktop_hwnd)

    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
    style = style | WS_CHILD | WS_VISIBLE
    SetWindowLong(hwnd, GWL_STYLE, style)

    move_window_bottom(root)


def restore_window(root: tk.Tk):
    root.overrideredirect(False)
    root.update_idletasks()
    hwnd = int(root.frame(), 16)

    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
    style = style & ~WS_CHILD
    SetWindowLong(hwnd, GWL_STYLE, style)
    SetParent(hwnd, 0)
