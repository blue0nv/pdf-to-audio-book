import tkinter as tk
from src.gui import AudiobookGUI

def main():
    root = tk.tk()
    app = AudiobookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()