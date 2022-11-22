"""
IS3020

@author: David Thomas
"""

import pickle
import copy
import os
from datetime import date
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog

#add food to save file to track
def addFood():
    try:
        file = open('save.pkl', 'rb')
        out = pickle.load(file)
        new = copy.copy(out)
        file.close()
        os.remove('save.pkl')
        foodName = input('enter food: ')
        print('enter experation date:')
        year = int(input('year: '))
        month = int(input('month: '))
        days = int(input('day: '))
        exp = datetime.date(year,month,days)
        exp2 = exp
        new.update({foodName : exp2})
        file = open('save.pkl', 'wb')
        pickle.dump(new, file)
        file.close()
        print(foodName, 'added')
    except FileNotFoundError:
        newSave()
        addFood()

#list all food in pantry
def listFood():
    try:
        print('food in pantry:')
        file = open('save.pkl', 'rb')
        out = pickle.load(file)
        for keys in out.keys():
            print(keys)
    except FileNotFoundError:
        print('File does not exist. Create New Save file.')    

#delete a food item from dictionary
def delFood():
    file = open('save.pkl', 'rb')
    out = pickle.load(file)
    new = copy.copy(out)
    print('current food in pantry:')
    file.close()
    for keys in new.keys():
        print(keys)
    os.remove('save.pkl')
    foodName = input('enter food to delete: ')
    try:
        new.pop(foodName)
    except KeyError:
        print(foodName, 'not found')
    file = open('save.pkl', 'wb')
    pickle.dump(new, file)
    file.close()
    print(foodName, 'deleted')
    

#deletes save file
def deleteSave():
    try:
        os.remove('save.pkl')
    except FileNotFoundError:
        print('save file does not exist')


#create a new save file
def newSave():
    food = {}
    file = open('save.pkl', 'wb')
    pickle.dump(food,file)
    file.close()
    

#check for expired food
def checkDates():
    file = open('save.pkl', 'rb')
    try:
        filePath = open('expOp.pkl', 'rb')
        filePath2 = pickle.load(filePath)
        filePath3 = filePath2 + '\list.txt'
        file2 = open(filePath3, 'a')
    except FileNotFoundError:
        file2 = open('list.txt', 'a')
    expiredList = []
    out = pickle.load(file)
    new = copy.copy(out)
    file.close()
    try:
        for key, value in new.items():
            if value <= date.today():
                print(key)
                expiredList.append(key)
                os.remove('save.pkl')
                new.pop(key)
                file = open('save.pkl', 'wb')
                pickle.dump(new, file)
                file2.writelines(expiredList)
                file2.writelines('\n')
                file.close()
                file2.close()
    except RuntimeError:
        checkDates()
        
    

def setExpFolder():
    tk.Tk().withdraw() # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory()
    file = open('expOp.pkl', 'wb')
    pickle.dump(folder_path, file)
    file.close()
    

#GUI using tkinter
class App:
    def __init__(self, root):
        #setting title
        root.title("Food Tracker")
        #setting window size
        width=272
        height=284
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_912=tk.Button(root)
        GButton_912["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_912["font"] = ft
        GButton_912["fg"] = "#000000"
        GButton_912["justify"] = "center"
        GButton_912["text"] = "Add Food"
        GButton_912.place(x=10,y=10,width=101,height=52)
        GButton_912["command"] = self.GButton_912_command

        GButton_601=tk.Button(root)
        GButton_601["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_601["font"] = ft
        GButton_601["fg"] = "#000000"
        GButton_601["justify"] = "center"
        GButton_601["text"] = "Delete Food"
        GButton_601.place(x=10,y=80,width=101,height=52)
        GButton_601["command"] = self.GButton_601_command

        GButton_936=tk.Button(root)
        GButton_936["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_936["font"] = ft
        GButton_936["fg"] = "#000000"
        GButton_936["justify"] = "center"
        GButton_936["text"] = "Check Dates"
        GButton_936.place(x=10,y=150,width=101,height=52)
        GButton_936["command"] = self.GButton_936_command

        GButton_369=tk.Button(root)
        GButton_369["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_369["font"] = ft
        GButton_369["fg"] = "#000000"
        GButton_369["justify"] = "center"
        GButton_369["text"] = "List Food"
        GButton_369.place(x=10,y=220,width=101,height=52)
        GButton_369["command"] = self.GButton_369_command

        GLabel_601=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_601["font"] = ft
        GLabel_601["fg"] = "#333333"
        GLabel_601["justify"] = "center"
        GLabel_601["text"] = "Settings:"
        GLabel_601.place(x=150,y=20,width=70,height=25)

        GButton_63=tk.Button(root)
        GButton_63["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_63["font"] = ft
        GButton_63["fg"] = "#000000"
        GButton_63["justify"] = "center"
        GButton_63["text"] = "New Save"
        GButton_63.place(x=160,y=80,width=101,height=52)
        GButton_63["command"] = self.GButton_63_command

        GButton_104=tk.Button(root)
        GButton_104["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_104["font"] = ft
        GButton_104["fg"] = "#000000"
        GButton_104["justify"] = "center"
        GButton_104["text"] = "Delete Save"
        GButton_104.place(x=160,y=150,width=101,height=52)
        GButton_104["command"] = self.GButton_104_command

        GButton_880=tk.Button(root)
        GButton_880["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_880["font"] = ft
        GButton_880["fg"] = "#000000"
        GButton_880["justify"] = "center"
        GButton_880["text"] = "Set Folder"
        GButton_880.place(x=160,y=220,width=101,height=52)
        GButton_880["command"] = self.GButton_880_command

    def GButton_912_command(self):
        addFood()


    def GButton_601_command(self):
        delFood()


    def GButton_936_command(self):
        checkDates()


    def GButton_369_command(self):
        listFood()


    def GButton_63_command(self):
        newSave()


    def GButton_104_command(self):
        deleteSave()


    def GButton_880_command(self):
        setExpFolder()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
        


