import pickle
import copy
import os
from datetime import date
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import tkinter as tk
import tkinter.font as tkFont


sched = BlockingScheduler()
@sched.scheduled_job('interval', seconds=5)

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


sched.start()


class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=215
        height=76
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_174=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_174["font"] = ft
        GLabel_174["fg"] = "#333333"
        GLabel_174["justify"] = "center"
        GLabel_174["text"] = "close to stop autoCheck"
        GLabel_174.place(x=10,y=20,width=183,height=33)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()





