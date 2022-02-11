import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from pandas import *
import pathlib
import webbrowser

data = read_csv("bbc_headlines.csv")
headlinelist = data['Headline'].tolist()
urlList = data['URL'].tolist()


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "WindowBlueprint.ui")


class DesignerOneApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('toplevel2', master)
        builder.connect_callbacks(self)
        
    

    def on_news1_clicked(self):
        print('uno')
        pass  
    

    def on_news2_clicked(self):
        print('dos')
        pass

    def on_news3_clicked(self):
        print('tres')
        pass

    def on_news4_clicked(self):
        print('cuatro')
        pass

    def on_papers_clicked(self):
        print('papel')
        pass

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = DesignerOneApp()
    app.run()