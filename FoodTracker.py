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
    print(new)
    main()

#delete a food item from dictionary
def delFood():
    file = open('save.pkl', 'rb')
    out = pickle.load(file)
    new = copy.copy(out)
    file.close()
    os.remove('save.pkl')
    foodName = input('enter food to delete: ')
    new.pop(foodName)
    file = open('save.pkl', 'wb')
    pickle.dump(new, file)
    file.close()
    print(new)
    main()

#deletes save file
def deleteSave():
    try:
        os.remove('save.pkl')
        main()
    except FileNotFoundError:
        main()


#create a new save file
def newSave():
    food = {}
    file = open('save.pkl', 'wb')
    pickle.dump(food,file)
    file.close()
    main()

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
    main()

def setExpFolder():
    setPath = input('file path of expired food list: ')
    file = open('expOp.pkl', 'wb')
    pickle.dump(setPath, file)
    file.close()
    main()


def settings():
    select = int(input('what do you want to set? \n1. Set folder for expired foods \n'))
    if select == 1:
        setExpFolder()
    elif select == exit:
        main()
#menu listing all of options for the user
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



main()