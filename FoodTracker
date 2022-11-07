"""
IS3020

@author: David Thomas
"""

import pickle
import copy
import os
from datetime import date
import datetime

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

def deleteSave ():
    try:
        os.remove('save.pkl')
        main()
    except FileNotFoundError:
        main()

def newSave():
    food = {}
    file = open('save.pkl', 'wb')
    pickle.dump(food,file)
    file.close()
    main()


def main():
    select = int(input('what action do you want to do?\n1. add new food \n2. delete save \n3. new save\n'))
    if select == 1:
        addFood()
    elif select == 2:
        deleteSave()
    elif select == 3:
        newSave()
    else:
        print('enter numbers 1-3')
        main()

main()
