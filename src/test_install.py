# src/test_install.py
import sys
import tkinter
import pygame

print("Python-Version:", sys.version)
print("tkinter-Version:", tkinter.TkVersion)
print("pygame-Version:", pygame.__version__)

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Testfenster")
    root.mainloop()
