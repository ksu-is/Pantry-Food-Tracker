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

#add food to save file to track
def addFood():
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

#list all food in pantry
def listFood():
    file = open('save.pkl', 'rb')
    out = pickle.load(file)
    for keys in out.keys():
        print(keys)    

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
        
def startautocheck():
    import autoCheck
    

def setExpFolder():
    setPath = input('file path of expired food list: ')
    file = open('expOp.pkl', 'wb')
    pickle.dump(setPath, file)
    file.close()
    

"""
def settings():
    select = int(input('what do you want to set? \n1. Set folder for expired foods \n'))
    if select == 1:
        setExpFolder()
    elif select == exit:
        main()"""
        
class App:
    def __init__(self, root):
        #setting title
        root.title("Food Tracker")
        #setting window size
        width=307
        height=256
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_106=tk.Button(root)
        GButton_106["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_106["font"] = ft
        GButton_106["fg"] = "#000000"
        GButton_106["justify"] = "center"
        GButton_106["text"] = "Add food"
        GButton_106.place(x=20,y=50,width=70,height=25)
        GButton_106["command"] = self.GButton_106_command

        GButton_576=tk.Button(root)
        GButton_576["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_576["font"] = ft
        GButton_576["fg"] = "#000000"
        GButton_576["justify"] = "center"
        GButton_576["text"] = "Delete Save"
        GButton_576.place(x=220,y=130,width=70,height=25)
        GButton_576["command"] = self.GButton_576_command

        GButton_281=tk.Button(root)
        GButton_281["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_281["font"] = ft
        GButton_281["fg"] = "#000000"
        GButton_281["justify"] = "center"
        GButton_281["text"] = "New Save"
        GButton_281.place(x=220,y=90,width=70,height=25)
        GButton_281["command"] = self.GButton_281_command

        GButton_689=tk.Button(root)
        GButton_689["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_689["font"] = ft
        GButton_689["fg"] = "#000000"
        GButton_689["justify"] = "center"
        GButton_689["text"] = "Delete Food"
        GButton_689.place(x=20,y=90,width=70,height=25)
        GButton_689["command"] = self.GButton_689_command

        GButton_448=tk.Button(root)
        GButton_448["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_448["font"] = ft
        GButton_448["fg"] = "#000000"
        GButton_448["justify"] = "center"
        GButton_448["text"] = "Check Dates"
        GButton_448.place(x=20,y=130,width=70,height=25)
        GButton_448["command"] = self.GButton_448_command

        GButton_713=tk.Button(root)
        GButton_713["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=8)
        GButton_713["font"] = ft
        GButton_713["fg"] = "#000000"
        GButton_713["justify"] = "center"
        GButton_713["text"] = "Start autoCheck"
        GButton_713.place(x=20,y=170,width=80,height=34)
        GButton_713["command"] = self.GButton_713_command

        GButton_104=tk.Button(root)
        GButton_104["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_104["font"] = ft
        GButton_104["fg"] = "#000000"
        GButton_104["justify"] = "center"
        GButton_104["text"] = "Set folder"
        GButton_104.place(x=220,y=170,width=70,height=25)
        GButton_104["command"] = self.GButton_104_command

        GLabel_737=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#333333"
        GLabel_737["justify"] = "center"
        GLabel_737["text"] = "Settings"
        GLabel_737.place(x=210,y=50,width=70,height=25)

        GButton_135=tk.Button(root)
        GButton_135["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_135["font"] = ft
        GButton_135["fg"] = "#000000"
        GButton_135["justify"] = "center"
        GButton_135["text"] = "List Food"
        GButton_135.place(x=20,y=220,width=70,height=25)
        GButton_135["command"] = self.GButton_135_command

    def GButton_106_command(self):
        addFood()


    def GButton_576_command(self):
        deleteSave()


    def GButton_281_command(self):
        newSave()

    def GButton_689_command(self):
        delFood()


    def GButton_448_command(self):
        checkDates()


    def GButton_713_command(self):
        startautocheck()

    def GButton_449_command(self):
        checkDates()

    def GButton_104_command(self):
        setExpFolder()

    def GButton_135_command(self):
        listFood()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
        


#menu listing all of options for the user
"""
def main():
    select = int(input('what action do you want to do?\n1. add new food \n2. delete save \n3. new save \n4.Check dates \n5. Remove a food item \n6. start auto checker \n7. settings\n'))
    if select == 1:
        addFood()
    elif select == 2:
        deleteSave()
    elif select == 3:
        newSave()
    elif select == 4:
        checkDates()
    elif select == 5:
        delFood()
    elif select == 6:
        startautocheck()
    elif select == 7:
        settings()
    else:
        print('enter numbers 1-6')
        main()
"""

