import pathlib
import tkinter as tk
import tkinter.ttk as ttk
from pandas import *
import webbrowser

data = read_csv("bbc_headlines.csv")
headlinelist = data['Headline'].tolist()
urlList = data['URL'].tolist()

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "BBCtkBlueprint.ui"

class BbctkblueprintApp:
    def __init__(self, master=None):
        # build ui
        self.uptop = tk.Tk() if master is None else tk.Toplevel(master)
        self.lowerframe = tk.Frame(self.uptop)
        self.label1 = ttk.Label(self.lowerframe)

        self.story1_var = tk.StringVar(value=headlinelist[0])
        self.label1.configure(textvariable=self.story1_var)

        self.label1.place(anchor='nw', relx='0.05', rely='0.1', width='300', x='0', y='0')
        self.button1 = ttk.Button(self.lowerframe)
        self.button1.configure(text='Story link')
        self.button1.place(anchor='nw', relx='0.75', rely='0.09', x='0', y='0')
        self.button1.configure(command=self.on_story1_click)
        self.label2 = ttk.Label(self.lowerframe)

        self.story2_var = tk.StringVar(value=headlinelist[1])
        self.label2.configure(textvariable=self.story2_var)

        self.label2.place(anchor='nw', relx='0.05', rely='0.2', width='300', x='0', y='0')
        self.label3 = ttk.Label(self.lowerframe)

        self.story3_var = tk.StringVar(value=headlinelist[2])
        self.label3.configure(textvariable=self.story3_var)

        self.label3.place(anchor='nw', relx='0.05', rely='0.3', width='300', x='0', y='0')
        self.label4 = ttk.Label(self.lowerframe)

        self.story4_var = tk.StringVar(value=headlinelist[3])
        self.label4.configure(textvariable=self.story4_var)

        self.label4.place(anchor='nw', relx='0.05', rely='0.4', width='300', x='0', y='0')
        self.label5 = ttk.Label(self.lowerframe)

        self.story5_var = tk.StringVar(value=headlinelist[4])
        self.label5.configure(textvariable=self.story5_var)

        self.label5.place(anchor='nw', relx='0.05', rely='0.5', width='300', x='0', y='0')
        self.label6 = ttk.Label(self.lowerframe)

        self.story6_var = tk.StringVar(value=headlinelist[5])
        self.label6.configure(textvariable=self.story6_var) 

        self.label6.place(anchor='nw', relx='0.05', rely='0.6', width='300', x='0', y='0')
        self.label7 = ttk.Label(self.lowerframe)

        self.story7_var = tk.StringVar(value=headlinelist[6])
        self.label7.configure(textvariable=self.story7_var)

        self.label7.place(anchor='nw', relx='0.05', rely='0.7', width='300', x='0', y='0')
        self.label8 = ttk.Label(self.lowerframe)

        self.story8_var = tk.StringVar(value=headlinelist[7])
        self.label8.configure(textvariable=self.story8_var)

        self.label8.place(anchor='nw', relx='0.05', rely='0.8', width='300', x='0', y='0')
        self.label9 = ttk.Label(self.lowerframe)

        self.story9_var = tk.StringVar(value=headlinelist[8])
        self.label9.configure(textvariable=self.story9_var)

        self.label9.place(anchor='nw', relx='0.05', rely='0.9', width='300', x='0', y='0')
        self.button2 = ttk.Button(self.lowerframe)
        self.button2.configure(text='Story link')
        self.button2.place(anchor='nw', relx='0.75', rely='0.19', x='0', y='0')
        self.button2.configure(command=self.on_story2_click)
        self.button3 = ttk.Button(self.lowerframe)
        self.button3.configure(text='Story link')
        self.button3.place(anchor='nw', relx='0.75', rely='0.39', x='0', y='0') 
        self.button3.configure(command=self.on_story4_click)
        self.button4 = ttk.Button(self.lowerframe)
        self.button4.configure(text='Story link')
        self.button4.place(anchor='nw', relx='0.75', rely='0.29', x='0', y='0')
        self.button4.configure(command=self.on_story3_click)
        self.button5 = ttk.Button(self.lowerframe)
        self.button5.configure(text='Story link')
        self.button5.place(anchor='nw', relx='0.75', rely='0.49', x='0', y='0')
        self.button5.configure(command=self.on_story5_click)
        self.button6 = ttk.Button(self.lowerframe)
        self.button6.configure(text='Story link')
        self.button6.place(anchor='nw', relx='0.75', rely='0.59', x='0', y='0')
        self.button6.configure(command=self.on_story6_click)
        self.button7 = ttk.Button(self.lowerframe)
        self.button7.configure(text='Story link')
        self.button7.place(anchor='nw', relx='0.75', rely='0.69', x='0', y='0')
        self.button7.configure(command=self.on_story7_click)
        self.button8 = ttk.Button(self.lowerframe)
        self.button8.configure(text='Story link')
        self.button8.place(anchor='nw', relx='0.75', rely='0.79', x='0', y='0')
        self.button8.configure(command=self.on_story8_click)
        self.button9 = ttk.Button(self.lowerframe)
        self.button9.configure(text='Story link')
        self.button9.place(anchor='nw', relx='0.75', rely='0.89', x='0', y='0')
        self.button9.configure(command=self.on_story9_click)
        self.label10 = ttk.Label(self.lowerframe)
        self.label10.configure(background='#ffffff', font='{Arial} 20 {}', text='BBC Stories')
        self.label10.place(anchor='nw', relx='0.35', x='0', y='0')
        self.lowerframe.configure(background='#ffffff', height='500', width='500')
        self.lowerframe.place(anchor='nw', x='0', y='0')
        self.uptop.configure(height='500', relief='flat', width='500')

        # Main widget
        self.mainwindow = self.uptop
    
    def run(self):
        self.mainwindow.mainloop()

    def on_story1_click(self):
        webbrowser.open(urlList[0])
        pass

    def on_story2_click(self):
        webbrowser.open(urlList[1])
        pass


    def on_story3_click(self):
        webbrowser.open(urlList[2])
        pass

    def on_story4_click(self):
        webbrowser.open(urlList[3])
        pass

    def on_story5_click(self):
        webbrowser.open(urlList[4])
        pass

    def on_story6_click(self):
        webbrowser.open(urlList[5])
        pass

    def on_story7_click(self):
        webbrowser.open(urlList[6])
        pass

    def on_story8_click(self):
        webbrowser.open(urlList[7])
        pass

    def on_story9_click(self):
        webbrowser.open(urlList[8])
        pass

if __name__ == '__main__':
    app = BbctkblueprintApp()
    app.run()