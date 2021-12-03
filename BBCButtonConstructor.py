import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
import csv
from pandas import *

data = read_csv("bbc_headlines.csv")
headlinelist = data['Headline'].tolist()


PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "BBCtkBlueprint.ui"


class BbctkblueprintApp:
    def __init__(self, master=None):
        # build ui
        self.uptop = tk.Tk() if master is None else tk.Toplevel(master)
        self.lowerframe = tk.Frame(self.uptop)
        self.label1 = ttk.Label(self.lowerframe)

        self.entry1_var = tk.StringVar(value=headlinelist[0])
        self.label1.configure(textvariable=self.entry1_var)
        
        self.label1.place(anchor='nw', relx='0.3', rely='0.1', width='300', x='0', y='0')
        self.lowerframe.configure(background='#ffffff', height='500', width='500')
        self.lowerframe.place(anchor='nw', x='0', y='0')
        self.uptop.configure(height='500', relief='flat', width='500')

        # Main widget
        self.mainwindow = self.uptop
    
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = BbctkblueprintApp()
    app.run()

