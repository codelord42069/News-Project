import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from pandas import *

data = read_csv("bbc_headlines.csv")
headlinelist = data['Headline'].tolist()
urlList = data['URL'].tolist()

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "WindowBlueprint.ui")

feedbacksubmitted = False
feedbacknums = []

import timeit
start = timeit.default_timer()

class WindowblueprintApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)

        self.mainwindow = builder.get_object('toplevel2', master)
        
        self.slider_var = None
        self.feedback_name = None
        global feedbacksubmitted
        feedbacksubmitted = False
    
        stop = timeit.default_timer()

        print('Time: ', stop - start)  
       
        builder.import_variables(self, ['slider_var', 'feedback_name'])

        builder.connect_callbacks(self)
    
    def run(self):
        self.mainwindow.mainloop()

    def on_news1_clicked(self):
        os.system('BBCButtonONCLICK.py')
        pass

    def on_news2_clicked(self):
        os.system('DailyMailONCLICK.py')
        pass

    def on_news3_clicked(self):
        os.system('GuardianONCLICK.py')
        pass

    def on_news4_clicked(self):
        os.system('independentONCLICK.py')
        pass

    def slider_callback(self, scale_value):
        pass

    def on_submit_feedback_pressed(self):

        global feedbacksubmitted
        if feedbacksubmitted == False:

            if not self.builder.tkvariables['feedback_name'].get().isalpha(): 
                print('Name Invalid!')
            else:
            
                print(self.builder.tkvariables['slider_var'].get())
                print(self.builder.tkvariables['feedback_name'].get())

                feedbackstring = 'Rated ' + str(self.builder.tkvariables['slider_var'].get()) + ' by ' + str(self.builder.tkvariables['feedback_name'].get())
                print(feedbackstring)

                f = open("feedback.txt", "a")
                f.write('\n')
                f.write(feedbackstring)
                f.close()

                feedbacknums.append(int(self.builder.tkvariables['slider_var'].get()))

                print('Average rating is ' + (str((sum(feedbacknums)/len(feedbacknums)))))
                feedbacksubmitted = True

        elif feedbacksubmitted == True:
            print('Feedback already submitted')


        pass

if __name__ == '__main__':
    app = WindowblueprintApp()
    app.run()







