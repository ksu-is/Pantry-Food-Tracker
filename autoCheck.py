import pickle
import copy
import os
from datetime import date
from win10toast import ToastNotifier
from apscheduler.schedulers.blocking import BlockingScheduler


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
                notification()
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

toast = ToastNotifier()
def notification():
    toast.show_toast(
        'food expired',
        'food added to shopping list',
        duration = 20,
        threaded = True,
    )

sched.start()



