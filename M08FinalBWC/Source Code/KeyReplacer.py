"""
Program: KeyReplacer
Author: Braeden Cunningham
Description: KeyReplacer is a python program that uses tkinter to create a user interface. This program allows the user to create an order
             for keys on a keyboard that they would like to replace. The user also needs to add their information for the order to be 
             successfully completed.
DLM: 05/12/2024
"""

import tkinter as tk
from MainWindow import MainWindow
from KeyboardWindow import KeyboardWindow
from PurchaseWindow import PurchaseWindow

def main():
    """This a function to run the entire program."""
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

# executes the program
if __name__ == "__main__":
    main()