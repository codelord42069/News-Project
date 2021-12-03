import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "WindowBlueprint2.ui"


class Windowblueprint2App:
    def __init__(self, master=None):
        # build ui
        self.uptop = tk.Tk() if master is None else tk.Toplevel(master)
        self.lowerframe = tk.Frame(self.uptop)
        self.lowerframe.configure(background='#ffffff', height='500', width='500')
        self.lowerframe.place(anchor='nw', x='0', y='0')
        self.uptop.configure(height='500', relief='flat', width='500')

        # Main widget
        self.mainwindow = self.uptop
    
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = Windowblueprint2App()
    app.run()
